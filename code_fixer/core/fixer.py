"""
Applies fixes to detected code issues.
"""
import re
from typing import Dict
from .base import BaseFixer
from .errors import FixerError
from ..utils.text import safe_split_lines, safe_join_lines

class CodeFixer(BaseFixer):
    def __init__(self, rules: Dict):
        self.rules = rules
    
    def fix_line(self, line: str) -> str:
        """Apply fixes to a single line of code."""
        try:
            fixed_line = line
            for rule in self.rules.values():
                if rule.get('fix') is not None:
                    fixed_line = re.sub(rule['pattern'], rule['fix'], fixed_line)
            return fixed_line
        except Exception as e:
            raise FixerError(f"Error fixing line: {str(e)}")
    
    def fix_code(self, content: str) -> str:
        """Fix code content."""
        try:
            lines = safe_split_lines(content)
            fixed_lines = [self.fix_line(line) for line in lines]
            return safe_join_lines(fixed_lines)
        except Exception as e:
            raise FixerError(f"Error fixing code: {str(e)}")