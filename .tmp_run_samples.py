import asyncio
from pathlib import Path
from io import BytesIO
from app.services.document_processor import DocumentProcessor
from app.services.excel_service import ExcelService

FILES = [
    "Grupa Kety - 49716.pdf",
    "Pan Global - QAM-S40004.pdf",
    "PROSOFT - 04-2602846.pdf",
]

async def main():
    processor = DocumentProcessor()
    for name in FILES:
        path = Path("sample_pdfs") / name
        try:
            page_count, invoices = await processor.process_document(path.read_bytes())
            line_items = sum(len(inv.lineItems) for inv in invoices)
            excel_bytes = ExcelService.generate_workbook_bytes(invoices) if invoices else b""
            print(f"OK | {name} | pages={page_count} invoices={len(invoices)} line_items={line_items} excel_bytes={len(excel_bytes)}")
            for inv in invoices:
                print(f"  invoice={inv.invoiceNumber} items={len(inv.lineItems)} total={inv.header.totalAmount}")
        except Exception as e:
            print(f"ERR | {name} | {type(e).__name__}: {e}")

asyncio.run(main())
