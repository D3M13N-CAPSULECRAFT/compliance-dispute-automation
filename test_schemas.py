import unittest
from schemas import DisputePayload, SeverityLevel

class TestDisputePayload(unittest.TestCase):
    def test_valid_payload(self):
        payload = DisputePayload(
            dispute_id="DSP-10293",
            entity_id="NODE-ALPHA-01",
            reason="State controller timeout mismatch",
            severity="HIGH"
        )
        self.assertEqual(payload.severity, SeverityLevel.HIGH)
        self.assertEqual(payload.to_dict()["dispute_id"], "DSP-10293")

    def test_invalid_dispute_id(self):
        with self.assertRaises(ValueError):
            DisputePayload(
                dispute_id="INVALID-123",
                entity_id="NODE-ALPHA-01",
                reason="Testing invalid ID",
                severity="LOW"
            )

    def test_invalid_severity(self):
        with self.assertRaises(ValueError):
            DisputePayload(
                dispute_id="DSP-99999",
                entity_id="NODE-ALPHA-01",
                reason="Testing invalid severity",
                severity="EXTREME"
            )

    def test_empty_entity_id(self):
        with self.assertRaises(ValueError):
            DisputePayload(
                dispute_id="DSP-88888",
                entity_id="   ",
                reason="Testing blank entity ID",
                severity="LOW"
            )

if __name__ == "__main__":
    unittest.main()
