from fastapi import FastAPI, UploadFile, File
from typing import List
from orchestrator import process_claim_workflow

app = FastAPI(title="SuperClaims Backend")


@app.post("/process-claim")
async def process_claim(files: List[UploadFile] = File(...)):
    """
    Main endpoint:
    - Accepts multiple PDFs
    - Sends files to orchestrator
    - Returns structured JSON + claim decision
    """
    result = await process_claim_workflow(files)
    return result