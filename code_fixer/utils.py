"""
Utility functions for code fixing operations.
"""
from typing import List, Dict, Optional

def safe_split_lines(content: str) -> List[str]:
    """Safely split content into lines."""
    return content.splitlines(keepends=True)

def safe_join_lines(lines: List[str]) -> str:
    """Safely join lines back into content."""
    return ''.join(lines)

def format_issue(issue: Dict) -> str:
    """Format an issue for display."""
    return f"Line {issue['line']}: {issue['message']}\n  {issue['text']}"