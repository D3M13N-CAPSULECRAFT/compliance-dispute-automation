from enum import Enum, auto
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class ActionReason(Enum):
    USER_REQUEST = auto()
    IDLE_TIMEOUT = auto()
    POLICY_ENFORCEMENT = auto()
    COMPLIANCE_DISPUTE_TRIGGER = auto()

class Action(Enum):
    IDLE = auto()
    DIMMED = auto()
    SUSPEND = auto()
    SHUT_DOWN = auto()

class StateController:
    """
    Python implementation matching ChromiumOS powerd StateController 
    transition logic for compliance dispute verification workflows.
    """
    def __init__(self):
        self.current_state = Action.IDLE

    def update_state(self, target_action: Action, reason: ActionReason) -> Action:
        logging.info(f"UpdateState called: transitioning from {self.current_state.name} -> {target_action.name} (Reason: {reason.name})")
        self.current_state = target_action
        return self.current_state

if __name__ == "__main__":
    controller = StateController()
    controller.update_state(Action.SUSPEND, ActionReason.COMPLIANCE_DISPUTE_TRIGGER)
