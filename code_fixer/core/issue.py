"""
Issue data structure and formatting.
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class CodeIssue:
    line: int
    rule: str
    message: str
    text: str
    
    def format(self) -> str:
        """Format the issue for display."""
        return f"Line {self.line}: {self.message}\n  {self.text}"