class ClaimFormAgent:
    """
    Claim Form Agent:
    Extracts policy + patient details.
    """

    def run(self, fields: dict):
        return {
            "type": "claim_form",
            "name": fields.get("name"),
            "policy_number": "POL123456",
            "raw_text": fields.get("raw_text")
        }