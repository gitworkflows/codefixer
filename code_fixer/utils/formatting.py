"""
Formatting utilities for output.
"""
from typing import Dict

def format_issue(issue: Dict) -> str:
    """Format an issue for display."""
    try:
        return f"Line {issue['line']}: {issue['message']}\n  {issue['text']}"
    except Exception:
        return "Error formatting issue"