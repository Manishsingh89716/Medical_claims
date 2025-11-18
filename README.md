# SuperClaims – Automated Medical Claim Processing API

This is an AI-powered FastAPI backend that automatically processes medical insurance claim documents.  
Users upload multiple PDFs, and the system extracts data, classifies document types, validates claim consistency, and generates a final claim decision.

---

## 🚀 Features

- Upload **multiple PDFs** (claim form, id card, discharge summary, bill, etc.)
- **OCR-based text extraction** using PyPDF2
- **Document classification** via Gemini
- **Structured data extraction** using Gemini LLM
- **Automatic validation** of:
  - Missing required documents
  - Name mismatch  
  - Amount mismatch  
  - Date mismatch  
  - Diagnosis mismatch
- **Automatic claim decision**
  - `approved`
  - `manual_review`
  - `rejected`
- Clean JSON Output

---

## 📦 Installation

### 1. Clone the project
```bash
git clone <your-repo-url>
cd medical_claim_api
```

### 2. Create & activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Gemini API Key
#### Windows (PowerShell)
```powershell
setx GOOGLE_API_KEY "YOUR_GEMINI_KEY"
```

Restart terminal after this.

---

## ▶ Run the API

```bash
uvicorn main:app --reload
```

API opens at:

- Swagger UI → http://127.0.0.1:8000/docs  
- OpenAPI JSON → http://127.0.0.1:8000/openapi.json  

---

## 📌 Example Request (Swagger or cURL)

### **POST /process-claim**

Upload 4 PDFs:

```
claimform.pdf  
idcard.pdf  
discharge.pdf  
bill.pdf
```

### Example cURL:
```bash
curl -X POST "http://localhost:8000/process-claim" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "files=@claimform.pdf" \
  -F "files=@idcard.pdf" \
  -F "files=@discharge.pdf" \
  -F "files=@bill.pdf"
```

---

## 📌 Example JSON Response

```json
{
  "documents": [
    {
      "type": "bill",
      "name": "John Doe",
      "amount": 5000,
      "date": "2024-01-01",
      "raw_text": "Hospital Invoice Patient: John Doe Amount: 5000 Date: 2024-01-01"
    }
  ],
  "validation": {
    "missing_documents": [],
    "discrepancies": []
  },
  "claim_decision": {
    "status": "approved",
    "reason": "All documents are consistent."
  }
}
```

---

## ✔ Tech Stack

- **FastAPI**
- **Gemini 2.5 Flash**
- **PyPDF2**
- **Python 3.10+**

---