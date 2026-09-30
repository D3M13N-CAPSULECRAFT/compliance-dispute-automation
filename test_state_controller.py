import unittest
from state_controller import StateController, Action, ActionReason

class TestStateController(unittest.TestCase):
    def setUp(self):
        self.controller = StateController()

    def test_initial_state(self):
        self.assertEqual(self.controller.current_state, Action.IDLE)

    def test_state_transitions(self):
        result = self.controller.update_state(Action.SUSPEND, ActionReason.COMPLIANCE_DISPUTE_TRIGGER)
        self.assertEqual(result, Action.SUSPEND)
        self.assertEqual(self.controller.current_state, Action.SUSPEND)

if __name__ == "__main__":
    unittest.main()
