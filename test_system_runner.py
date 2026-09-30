import unittest
from system_runner import run_pipeline

class TestSystemRunner(unittest.TestCase):
    def test_pipeline_execution(self):
        success = run_pipeline()
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()
