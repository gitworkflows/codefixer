"""
Text processing utilities.
"""
from typing import List

def safe_split_lines(content: str) -> List[str]:
    """Safely split content into lines."""
    try:
        return content.splitlines(keepends=True)
    except Exception:
        return []

def safe_join_lines(lines: List[str]) -> str:
    """Safely join lines back into content."""
    try:
        return ''.join(lines)
    except Exception:
        return ''