import re
from dataclasses import dataclass, asdict
from enum import Enum
from typing import Optional, Dict, Any

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

        if not self.entity_id or not self.entity_id.strip():
            raise ValueError("entity_id cannot be empty")

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        if isinstance(self.severity, SeverityLevel):
            data["severity"] = self.severity.value
        return data
