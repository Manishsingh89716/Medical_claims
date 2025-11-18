class BillAgent:
    """
    Bill Agent:
    Converts LLM extracted fields into bill-specific JSON.
    """

    def run(self, fields: dict):
        return {
            "type": "bill",
            "amount": fields.get("amount"),
            "date": fields.get("date"),
            "name": fields.get("name"),
            "raw_text": fields.get("raw_text")
        }