from pathlib import Path
from app.services.pdf_service import PDFService
from app.services.ocr_service import OCRService
from app.models.page import TextSource
from app.services.invoice_extractor import InvoiceExtractor
from app.clients.llm_client import LLMClient

pdf_path = Path(r"c:\Users\abhis\Downloads\CUBIC - 6263375.pdf")

class DummyLLM(LLMClient):
    async def call(self, prompt: str) -> str:
        return '{"header":{},"lineItems":[]}'

pdf_service = PDFService()
ocr_service = OCRService()
pages = pdf_service.load_pages(pdf_path.read_bytes())
page = pages[0]
print('tables', len(page.tables))
for table in page.tables[:1]:
    grid = InvoiceExtractor._table_to_grid(table)
    for row in grid[:8]:
        print(row)
