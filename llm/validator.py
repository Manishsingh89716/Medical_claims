import os
import google.generativeai as genai
import json

genai.configure(api_key="your api key here")
#os.getenv("GOOGLE_API_KEY")
def validate_claims(documents: list) -> dict:
    prompt = f"""
    STRICT JSON ONLY.

    Required output:
    {{
      "missing_documents": [...],
      "discrepancies": [...]
    }}

    Documents:
    {json.dumps(documents)}
    """

    try:
        model = genai.GenerativeModel(
            "gemini-2.5-flash",
            generation_config={"response_mime_type": "application/json"}
        )

        response = model.generate_content(prompt)
        return json.loads(response.text)

    except Exception as e:
        print("Validation error:", e, "RAW:", getattr(e, 'response', None))
        return {
            "missing_documents": [],
            "discrepancies": []
        }