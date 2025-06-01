from langchain.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template("""
You are a helpful assistant. Extract the following information from the given invoice text:

- Invoice Date
- Customer Name
- Customer Billing Address
- Customer Shipping Address
- Item Names or IDs
- Quantity
- Invoice Number
- Final Amount

Return the result in JSON format like this:
{{
    "Invoice Date": "...",
    "Customer Name": "...",
    "Customer Billing Address": "...",
    "Customer Shipping Address": "...",
    "Item Names/IDs": [...],
    "Quantity": [...],
    "Invoice No.": "...",
    "Final Amount": "..."
}}
And finally make sure if there are multiple items and multiple quantity respectively then format them like how in json you do like the following.
"Quantity" : [
    "1.00",
    "2.00"
]. like this. Same with multiple name and ID available. 

And also if there's only one customer address present then the billing and shipping address is the same. If you find 2 addresses it may happen that the address is not of the one who was billed but of the company who sent the invoice and their company address, try and focus on which is which before taking in the address. You might have a single billing address but in the pdf the company adress is also present so you may wrongfully take that as shipping address. Try to be as careful as possible in those scenarios as possible. 

When checking for different item and item name id's try and look for where it is mapped to a quantity or if there is any denotation that there is an amount like that somewhere. Based on that choose the item and the corresponding quantity. 

Also make sure if you do not find something or you're in doubt of it then leave it blank, like in some cases you might not find something mentioned then just leave it blank instead of putting in that. 

If you find an item and don't see the number of items or amount mentioned then consider the quantity as 1 

Make sure not to return bold or italicised texts with '\n' or include / especially in Invoice number. 

Finally if you are extracting the amount just extract the number and no dollar or rupee or pound sign or text, just extract the amount number and that's it.

Invoice Text:
{invoice_text}
""")