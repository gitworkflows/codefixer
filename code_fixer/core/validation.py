"""
Input validation utilities.
"""
from typing import Optional
from .errors import ValidationError

def validate_code_input(code: str) -> None:
    """Validate code input string."""
    if not isinstance(code, str):
        raise ValidationError("Input must be a string")
    if not code.strip():
        raise ValidationError("Input code cannot be empty")