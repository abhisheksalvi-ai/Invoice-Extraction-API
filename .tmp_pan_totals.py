import asyncio
from pathlib import Path
from app.services.pdf_service import PDFService
from app.clients.ocr_client import AzureDocumentIntelligenceClient

async def main():
    path = Path('sample_pdfs') / 'Pan Global - QAM-S40004.pdf'
    doc = PDFService.open_pdf(path.read_bytes())
    page = doc.load_page(0)
    native = page.get_text('text')
    print('--- Native lines with total ---')
    nlines = [l.strip() for l in native.splitlines() if l.strip()]
    for i, l in enumerate(nlines):
        if 'total' in l.lower():
            print(i, l)

    img = PDFService.render_page_to_image(page)
    client = AzureDocumentIntelligenceClient()
    res = await client.analyze_document(img)
    print('--- OCR lines with total ---')
    olines = [l.strip() for l in (res.get('text') or '').splitlines() if l.strip()]
    for i, l in enumerate(olines):
        if 'total' in l.lower():
            print(i, l)

asyncio.run(main())
