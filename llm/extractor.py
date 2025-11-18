import os
import google.generativeai as genai
import json

genai.configure(api_key="your api key here")

def extract_document_fields(text: str) -> dict:
    prompt = f"""
    You MUST return STRICT JSON ONLY.

    Required fields:
    - name
    - amount
    - date
    - diagnosis
    - policy_number
    - raw_text

    Use null if missing.

    Respond example:
    {{
      "name": "John",
      "amount": 5500,
      "date": "2024-04-01",
      "diagnosis": "Fever",
      "policy_number": "ABC123",
      "raw_text": "..."
    }}

    Document:
    {text}
    """

    try:
        model = genai.GenerativeModel(
            "gemini-2.5-flash",
            generation_config={"response_mime_type": "application/json"}
        )

        response = model.generate_content(prompt)
        return json.loads(response.text)

    except Exception as e:
        print("Extraction error:", e, "RAW:", getattr(e, 'response', None))
        return {
            "name": None,
            "amount": None,
            "date": None,
            "diagnosis": None,
            "policy_number": None,
            "raw_text": text,
        }