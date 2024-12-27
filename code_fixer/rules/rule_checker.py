"""
Rule checking functionality.
"""
import re
from typing import Dict, List

class RuleChecker:
    @staticmethod
    def check_line(line: str, rule: Dict) -> bool:
        """Check if a line violates a rule."""
        try:
            return bool(re.search(rule['pattern'], line))
        except Exception:
            return False

    @staticmethod
    def apply_fix(line: str, rule: Dict) -> str:
        """Apply fix for a rule if available."""
        if not rule.get('fix'):
            return line
        try:
            return re.sub(rule['pattern'], rule['fix'], line)
        except Exception:
            return line