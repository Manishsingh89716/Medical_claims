class DischargeAgent:
    """
    Discharge Summary Agent:
    Parses discharge-specific fields from extracted text.
    """

    def run(self, fields: dict):
        return {
            "type": "discharge_summary",
            "date": fields.get("date"),
            "name": fields.get("name"),
            "diagnosis": "Not Available",
            "raw_text": fields.get("raw_text")
        }