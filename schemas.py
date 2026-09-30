import re
from dataclasses import dataclass
from enum import Enum
from typing import Optional

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
    timestamp: Optional[str] = None

    def __post_init__(self):
        if isinstance(self.severity, str):
            self.severity = SeverityLevel(self.severity)
            
        pattern = r"^DSP-\d{5}$"
        if not re.match(pattern, self.dispute_id):
            raise ValueError(
                f"Invalid dispute_id format: '{self.dispute_id}'. Must match pattern DSP-XXXXX"
            )
