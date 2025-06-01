from sqlalchemy import create_engine, Column, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
from datetime import datetime

Base = declarative_base()

class Memory(Base):
    __tablename__ = 'memory'
    thread_id = Column(String, primary_key=True)
    source = Column(String)
    type = Column(String)
    timestamp = Column(String)
    extracted_data = Column(Text)

class SharedMemory:
    def __init__(self, db_path="sqlite:///memory.db"):
        self.engine = create_engine(db_path, echo=False)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def save(self, thread_id, source, type, extracted_data):
        timestamp = datetime.now().isoformat()
        session = self.Session()
        try:
            invoice_no = extracted_data.get("Invoice No.", "") if isinstance(extracted_data, dict) else ""
            if invoice_no:
                existing_entry = session.query(Memory).filter(
                    Memory.extracted_data.ilike(f'%{invoice_no}%')
                ).first()
                if existing_entry:
                    existing_entry.source = source
                    existing_entry.type = type
                    existing_entry.timestamp = timestamp
                    existing_entry.extracted_data = json.dumps(extracted_data)
                    session.commit()
                    return existing_entry.thread_id

            memory_entry = session.query(Memory).filter_by(thread_id=thread_id).first()
            if memory_entry:
                memory_entry.source = source
                memory_entry.type = type
                memory_entry.timestamp = timestamp
                memory_entry.extracted_data = json.dumps(extracted_data)
            else:
                memory_entry = Memory(
                    thread_id=thread_id,
                    source=source,
                    type=type,
                    timestamp=timestamp,
                    extracted_data=json.dumps(extracted_data)
                )
                session.add(memory_entry)
            session.commit()
            return thread_id
        finally:
            session.close()

    def get(self, thread_id):
        session = self.Session()
        try:
            memory_entry = session.query(Memory).filter_by(thread_id=thread_id).first()
            if memory_entry:
                return (
                    memory_entry.thread_id,
                    memory_entry.source,
                    memory_entry.type,
                    memory_entry.timestamp,
                    memory_entry.extracted_data
                )
            return None
        finally:
            session.close()

    def get_all(self):
        session = self.Session()
        try:
            entries = session.query(Memory).all()
            return [(e.thread_id, e.source, e.type, e.timestamp, e.extracted_data) for e in entries]
        finally:
            session.close()