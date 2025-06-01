import imaplib
import email
import json
import uuid

class EmailFetcher:
    def __init__(self, imap_server, imap_user, imap_password, json_agent, memory):
        self.imap_server = imap_server
        self.imap_user = imap_user
        self.imap_password = imap_password
        self.json_agent = json_agent
        self.memory = memory

    def fetch_invoices(self):
        try:
            mail = imaplib.IMAP4_SSL(self.imap_server)
            mail.login(self.imap_user, self.imap_password)
            mail.select("inbox")

            _, data = mail.search(None, 'SUBJECT "invoice"')
            invoices = []
            for num in data[0].split():
                _, msg_data = mail.fetch(num, "(RFC822)")
                email_body = msg_data[0][1]
                msg = email.message_from_bytes(email_body)
                subject = msg["subject"]
                if "invoice" in subject.lower():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            payload = part.get_payload(decode=True).decode()
                            try:
                                json_data = json.loads(payload.strip())
                                thread_id = str(uuid.uuid4())
                                result = self.json_agent.process(json_data, thread_id, source="Email")
                                invoices.append((subject, result, thread_id))
                            except json.JSONDecodeError:
                                continue

                mail.store(num, '+FLAGS', '\Seen')
            mail.logout()
            return invoices
        except Exception as e:
            return [{"error": f"Email fetching failed: {str(e)}"}]