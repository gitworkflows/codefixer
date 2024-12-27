"""
Rule validation utilities.
"""
from typing import Dict
from ..core.errors import ValidationError

def validate_rule(rule: Dict) -> None:
    """Validate a single rule definition."""
    required_fields = {'pattern', 'message'}
    missing_fields = required_fields - set(rule.keys())
    
    if missing_fields:
        raise ValidationError(
            f"Rule is missing required fields: {', '.join(missing_fields)}"
        )