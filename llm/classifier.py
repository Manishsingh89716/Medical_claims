import os
import google.generativeai as genai
import json

genai.configure(api_key="your api key here")

def classify_document(text: str) -> str:
    prompt = f"""
    You MUST respond in STRICT JSON ONLY. No explanation.

    Task:
    Classify the document into one of:
    - bill
    - discharge_summary
    - id_card
    - pharmacy_bill
    - claim_form
    - other

    Respond only like:
    {{"type": "bill"}}

    Document:
    {text}
    """

    try:
        model = genai.GenerativeModel(
            "gemini-2.5-flash",
            generation_config={"response_mime_type": "application/json"}
        )

        response = model.generate_content(prompt)

        return json.loads(response.text)["type"]

    except Exception as e:
        print("Classification error:", e, "RAW:", getattr(e, 'response', None))
        return "other"