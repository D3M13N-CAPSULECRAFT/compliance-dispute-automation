from enum import Enum, auto
from audit_logger import setup_audit_logger, log_audit_event

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
    def __init__(self, logger=None):
        self.current_state = Action.IDLE
        self.logger = logger or setup_audit_logger()

    def update_state(self, target_action: Action, reason: ActionReason) -> Action:
        from_state = self.current_state.name
        to_state = target_action.name
        reason_str = reason.name

        self.current_state = target_action

        log_audit_event(
            self.logger,
            event_type="STATE_TRANSITION",
            message=f"Transitioned state from {from_state} to {to_state}",
            context={
                "from_state": from_state,
                "to_state": to_state,
                "reason": reason_str,
            }
        )
        return self.current_state

if __name__ == "__main__":
    controller = StateController()
    controller.update_state(Action.SUSPEND, ActionReason.COMPLIANCE_DISPUTE_TRIGGER)
