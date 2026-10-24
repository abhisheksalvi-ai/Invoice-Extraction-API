from pathlib import Path
import fitz

pdf_path = Path(r"c:\Users\abhis\Downloads\CUBIC - 6263375.pdf")
doc = fitz.open(stream=pdf_path.read_bytes(), filetype='pdf')
for i, page in enumerate(doc, start=1):
    text = page.get_text('text') or ''
    if 'COO' in text or 'ECCN' in text or 'HTS' in text:
        print('--- page', i, '---')
        for line in text.splitlines():
            if 'COO' in line or 'ECCN' in line or 'HTS' in line:
                print(line)
