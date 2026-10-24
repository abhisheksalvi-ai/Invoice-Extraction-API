import asyncio
from pathlib import Path
from app.services.pdf_service import PDFService
from app.clients.ocr_client import AzureDocumentIntelligenceClient
from app.services.invoice_extractor import InvoiceExtractor

async def main():
    path = Path('sample_pdfs') / 'Grupa Kety - 49716.pdf'
    doc = PDFService.open_pdf(path.read_bytes())
    page = doc.load_page(0)
    image = PDFService.render_page_to_image(page)
    client = AzureDocumentIntelligenceClient()
    result = await client.analyze_document(image)
    print('text_len', len(result.get('text','')))
    print('tables', len(result.get('tables', [])))
    for t_idx, t in enumerate(result.get('tables', [])[:1], 1):
        grid = InvoiceExtractor._table_to_grid(t)
        print('table', t_idx, 'rows', len(grid), 'cols', len(grid[0]) if grid else 0)
        for i, row in enumerate(grid[:45]):
            print(i, row)

asyncio.run(main())
