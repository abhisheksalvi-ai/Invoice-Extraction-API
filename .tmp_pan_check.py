import asyncio
from pathlib import Path
from app.services.document_processor import DocumentProcessor

async def main():
    path = Path('sample_pdfs') / 'Pan Global - QAM-S40004.pdf'
    processor = DocumentProcessor()
    page_count, invoices = await processor.process_document(path.read_bytes())
    print('page_count', page_count, 'invoices', len(invoices))
    for inv in invoices:
        print('invoiceNumber', inv.invoiceNumber)
        print('headerTotal', inv.header.totalAmount)
        print('lineItems', len(inv.lineItems))
        calc = sum((li.amount or 0) for li in inv.lineItems)
        print('lineTotal', calc)
        for i, li in enumerate(inv.lineItems[:20], 1):
            print(i, li.partNumber, li.quantity, li.unitPrice, li.amount)

asyncio.run(main())
