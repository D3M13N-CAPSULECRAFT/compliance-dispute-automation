import unittest
from bci_telemetry_engine import BCITelemetryEngine

class TestBCITelemetryEngine(unittest.TestCase):
    def setUp(self):
        self.engine = BCITelemetryEngine(node_id="TEST-NODE")

    def test_radius_sweep_equilibrium(self):
        packet = {"positive_val": 3.0, "negative_val": 3.0}
        result = self.engine.execute_radius_sweep(packet)
        self.assertEqual(result["status"], "EQUILIBRIUM_LOCKED")
        self.assertEqual(result["radius_sweep"], 0.0)

    def test_radius_sweep_deficit(self):
        packet = {"positive_val": 1.0, "negative_val": 3.0}
        result = self.engine.execute_radius_sweep(packet)
        self.assertEqual(result["status"], "DEFICIT_RECOVERY")

if __name__ == "__main__":
    unittest.main()
