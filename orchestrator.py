import asyncio
from utils.pdf_reader import extract_pdf_text
from llm.classifier import classify_document
from llm.extractor import extract_document_fields
from agents.bill_agent import BillAgent
from agents.discharge_agent import DischargeAgent
from agents.id_agent import IDAgent
from agents.claim_form_agent import ClaimFormAgent
from llm.validator import validate_claims


async def process_claim_workflow(files):
    """
    Orchestrator:
    Controls entire flow:
    1. Extract text
    2. Classify doc
    3. Run appropriate agent
    4. Validate all docs
    5. Generate final decision
    """

    documents_output = []
    doc_type_map = {
        "bill": BillAgent(),
        "discharge_summary": DischargeAgent(),
        "id_card": IDAgent(),
        "claim_form": ClaimFormAgent()
    }

    # Process each PDF asynchronously
    for file in files:
        pdf_bytes = await file.read()

        # Step 1: Extract raw text
        extracted_text = extract_pdf_text(pdf_bytes)

        # Step 2: LLM classification
        doc_type = classify_document(extracted_text)

        # Step 3: LLM field extraction
        extracted_fields = extract_document_fields(extracted_text)

        # Step 4: Run the correct Agent based on doc type
        if doc_type in doc_type_map:
            structured_json = doc_type_map[doc_type].run(extracted_fields)
        else:
            structured_json = {"type": "other", "raw_text": extracted_text}

        documents_output.append(structured_json)

    # Step 5: Validation across documents
    validation_result = validate_claims(documents_output)

    # Step 6: Final claim decision based on validation output
    if validation_result["missing_documents"]:
        status = "manual_review"
        reason = "Some documents are missing."
    elif validation_result["discrepancies"]:
        status = "manual_review"
        reason = "There are data inconsistencies across documents."
    else:
        status = "approved"
        reason = "All documents are consistent."

    return {
        "documents": documents_output,
        "validation": validation_result,
        "claim_decision": {
            "status": status,
            "reason": reason
        }
    }