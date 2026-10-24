from pathlib import Path
import fitz

path = Path('sample_pdfs') / 'PROSOFT - 04-2602846.pdf'
doc = fitz.open(stream=path.read_bytes(), filetype='pdf')
print('pages', doc.page_count)
for i in range(doc.page_count):
    page = doc.load_page(i)
    text = page.get_text('text') or ''
    print('\n=== PAGE', i+1, 'LEN', len(text), '===')
    lines = [ln for ln in text.splitlines() if ln.strip()]
    for ln in lines[:120]:
        print(ln)
