# Invoice Extraction API

A modular Python FastAPI service for extracting invoices from PDF documents and returning a Power Automate-friendly JSON response.

## Features

- Single `POST /extract-invoices` endpoint for whole-PDF processing
- Native PDF text extraction and Azure Document Intelligence OCR support
- Invoice page grouping across multiple pages
- Pydantic validation with structured responses
- Swagger documentation at `/docs`

## Installation

1. Create a Python 3.11+ virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate    # Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy environment variables:

```bash
cp .env.example .env
```

4. Set Azure and LLM configuration in `.env`.

> For local testing, you can point `LLM_ENDPOINT`/`LLM_API_KEY` to an OpenAI-compatible endpoint and keep production client settings separate.
> 
> The current implementation expects a request body with `model` and `prompt`, and returns the `text` field from the response.

## Running locally

```bash
python run.py
```

Then visit `http://127.0.0.1:8000/docs`.

## API Endpoints

- `GET /health` — health status
- `POST /extract-invoices` — upload a PDF in `multipart/form-data` with field `file`
- `POST /download-invoices` — upload a PDF in `multipart/form-data` with field `file` and download an Excel workbook of extracted invoices

## Sample curl

```bash
curl -X POST "http://127.0.0.1:8000/extract-invoices" \
  -F "file=@/path/to/invoices.pdf"
```

Download Excel from extracted invoices:
```bash
curl -X POST "http://127.0.0.1:8000/download-invoices" \
  -F "file=@/path/to/invoices.pdf" \
  --output extracted_invoices.xlsx
```

## Power Automate Integration

Use the response from `/extract-invoices` in Power Automate:

- Parse JSON from the HTTP response body
- Use `body('HTTP')?['invoices']`
- Loop through each invoice and create worksheets with `worksheetName`
