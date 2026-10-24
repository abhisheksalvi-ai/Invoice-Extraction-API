import asyncio
from pathlib import Path
from app.services.document_processor import DocumentProcessor

async def main():
    path = Path('sample_pdfs') / 'Grupa Kety - 49716.pdf'
    p = DocumentProcessor()
    page_count, invoices = await p.process_document(path.read_bytes())
    print('page_count', page_count, 'invoice_count', len(invoices))
    for i, inv in enumerate(invoices, 1):
        print('invoice', i, 'number', inv.invoiceNumber, 'total', inv.header.totalAmount, 'items', len(inv.lineItems))
        for li in inv.lineItems:
            print('  item=', li.itemNumber, 'part=', li.partNumber, 'qty=', li.quantity, 'uom=', li.uom, 'amount=', li.amount, 'desc=', (li.description or '')[:80])

asyncio.run(main())
