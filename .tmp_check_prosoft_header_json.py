from pathlib import Path
from fastapi.testclient import TestClient
from app.main import app

pdf = Path('sample_pdfs') / 'PROSOFT - 04-2602846.pdf'
client = TestClient(app)
resp = client.post('/extract-invoices', files={'file': (pdf.name, pdf.read_bytes(), 'application/pdf')})
print('status', resp.status_code)
body = resp.json()
inv = body['invoices'][0]
print(inv['header'])
