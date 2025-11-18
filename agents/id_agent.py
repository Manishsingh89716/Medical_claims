class IDAgent:
    """
    ID Card Agent:
    Extracts patient identity details.
    """
    def run(self, fields: dict):
        return {
            "type": "id_card",
            "name": fields.get("name"),
            "raw_text": fields.get("raw_text")
        }