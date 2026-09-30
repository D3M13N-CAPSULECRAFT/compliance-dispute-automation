import json
import logging
from datetime import datetime, timezone
from typing import Any, Dict, Optional

class JSONAuditFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_data: Dict[str, Any] = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "event_type": getattr(record, "event_type", "GENERAL"),
            "message": record.getMessage(),
        }
        
        # Include custom metadata context if present
        if hasattr(record, "audit_context") and isinstance(record.audit_context, dict):
            log_data["context"] = record.audit_context
            
        return json.dumps(log_data)

def setup_audit_logger(log_file: str = "audit.jsonl") -> logging.Logger:
    logger = logging.getLogger("compliance_audit")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Avoid adding duplicate handlers if logger is re-initialized
    if not logger.handlers:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(JSONAuditFormatter())
        logger.addHandler(file_handler)

    return logger

def log_audit_event(
    logger: logging.Logger, 
    event_type: str, 
    message: str, 
    context: Optional[Dict[str, Any]] = None
) -> None:
    extra = {
        "event_type": event_type,
        "audit_context": context or {}
    }
    logger.info(message, extra=extra)
