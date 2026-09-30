import json
import os
import unittest
from audit_logger import setup_audit_logger, log_audit_event

class TestAuditLogger(unittest.TestCase):
    def setUp(self):
        self.test_log = "test_audit.jsonl"
        if os.path.exists(self.test_log):
            os.remove(self.test_log)
        self.logger = setup_audit_logger(self.test_log)

    def tearDown(self):
        if os.path.exists(self.test_log):
            os.remove(self.test_log)

    def test_json_log_structure(self):
        log_audit_event(
            self.logger,
            event_type="TEST_EVENT",
            message="Verification test",
            context={"key": "value"}
        )

        with open(self.test_log, "r") as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 1)
            data = json.loads(lines[0])
            self.assertEqual(data["event_type"], "TEST_EVENT")
            self.assertEqual(data["message"], "Verification test")
            self.assertEqual(data["context"]["key"], "value")

if __name__ == "__main__":
    unittest.main()
