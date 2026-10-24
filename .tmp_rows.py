import asyncio
from pathlib import Path

from app.config import settings
from app.models.page import TextSource
from app.services.document_processor import DocumentProcessor

pdf_path = Path(r"c:\Users\abhis\Downloads\CUBIC - 6263375.pdf")


def table_to_grid(table):
    rc = table.get("row_count", 0)
    cc = table.get("column_count", 0)
    grid = [[""] * cc for _ in range(rc)]
    for cell in table.get("cells", []):
        r = cell.get("row_index", 0)
        c = cell.get("column_index", 0)
        if r < rc and c < cc:
            grid[r][c] = (cell.get("content") or "").strip()
    return grid

async def main():
    processor = DocumentProcessor()
    data = pdf_path.read_bytes()
    doc = processor.pdf_service.open_pdf(data)
    page = doc.load_page(0)
    native_text = processor.pdf_service.extract_text(page)
    if processor.ocr_service.should_use_ocr(native_text, settings.ocr_text_threshold):
        image_bytes = processor.pdf_service.render_page_to_image(page)
        processed_page = await processor.ocr_service.analyze_image(image_bytes, 1)
    else:
        processed_page = processor.pdf_service.build_page_model(1, native_text, TextSource.pdf_text)

    print(f"TABLES={len(processed_page.tables)}")
    for ti, t in enumerate(processed_page.tables, start=1):
        grid = table_to_grid(t)
        print(f"TABLE {ti} rows={len(grid)} cols={len(grid[0]) if grid else 0}")
        for i, row in enumerate(grid[:20], start=0):
            print(i, row)

asyncio.run(main())
