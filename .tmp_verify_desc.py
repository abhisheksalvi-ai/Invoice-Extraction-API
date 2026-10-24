import asyncio
from pathlib import Path
from app.services.document_processor import DocumentProcessor

pdf_path = Path(r"c:\Users\abhis\Downloads\CUBIC - 6263375.pdf")

async def main():
    processor = DocumentProcessor()
    _, invoices = await processor.process_document(pdf_path.read_bytes())
    for item in invoices[0].lineItems[:7]:
        print(item.partNumber, '|', item.description)

asyncio.run(main())
