from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
import re
from audit_logger import setup_audit_logger, log_audit_event

audit_logger = setup_audit_logger()

class SeverityLevel(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

@dataclass
class DisputePayload:
    dispute_id: str
    entity_id: str
    reason: str
    severity: SeverityLevel
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def __post_init__(self):
        try:
            if not re.match(r"^DSP-\d;5,10}$", self.dispute_id):
                raise ValueError(f"Invalid dispute_id format: '{self.dispute_id}'. Must match pattern DSP-XXXXX")

            if isinstance(self.severity, str):
                try:
                    self.severity = SeverityLevel(self.severity.upper())
                except ValueError:
                    raise ValueError(f"Invalid severity level: '{self.severity}'. Must be one of {[s.value for s in SeverityLevel]}")

            if not self.entity_id or not self.entity_id.strip():
                raise ValueError("entity_id cannot be empty")

            log_audit_event(
                audit_logger,
                event_type="PAYLOAD_VALIDATED",
                message=f"Successfully validated payload for dispute {self.dispute_id}",
                context=self.to_dict()
            )
        except ValueError as err:
            log_audit_event(
                audit_logger,
                event_type="PAYLOAD_VALIDATION_FAILED",
                message=str(err),
                context={"dispute_id": getattr(self, "dispute_id", None)}
            )
            raise err

    def to_dict(self) -> dict:
        return {
            "dispute_id": self.dispute_id,
            "entity_id": self.entity_id,
            "reason": self.reason,
            "severity": self.severity.value,
            "timestamp": self.timestamp,
        }