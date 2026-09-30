from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, auto
import re

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
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())

    def __post_init__(self):
        # Validate dispute_id format (e.g., DSP-XXXXX)
        if not re.match(r"^DSP-\d{5,10}$", self.dispute_id):
            raise ValueError(f"Invalid dispute_id format: '{self.dispute_id}'. Must match pattern DSP-XXXXX")

        # Normalize string severity into SeverityLevel Enum if passed as string
        if isinstance(self.severity, str):
            try:
                self.severity = SeverityLevel(self.severity.upper())
            except ValueError:
                raise ValueError(f"Invalid severity level: '{self.severity}'. Must be one of {[s.value for s in SeverityLevel]}")

        # Ensure entity_id is non-empty
        if not self.entity_id or not self.entity_id.strip():
            raise ValueError("entity_id cannot be empty")

    def to_dict(self) -> dict:
        return {
            "dispute_id": self.dispute_id,
            "entity_id": self.entity_id,
            "reason": self.reason,
            "severity": self.severity.value,
            "timestamp": self.timestamp,
        }
