from pathlib import Path
from fastapi.testclient import TestClient
from app.main import app

pdf = Path('sample_pdfs') / 'PROSOFT - 04-2602846.pdf'
client = TestClient(app)
resp = client.post('/extract-invoices', files={'file': (pdf.name, pdf.read_bytes(), 'application/pdf')})
print('status', resp.status_code)
body = resp.json()
inv = body['invoices'][0]
print('lineItems', len(inv['lineItems']))
for i, item in enumerate(inv['lineItems'], 1):
    print(i, {
        'partNumber': item.get('partNumber'),
        'expImpHts': item.get('expImpHts'),
        'countryOfOrigin': item.get('countryOfOrigin'),
        'eccnLicense': item.get('eccnLicense'),
        'ccatsErn': item.get('ccatsErn'),
        'unitPrice': item.get('unitPrice'),
        'amount': item.get('amount'),
    })
