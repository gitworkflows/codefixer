"""
Code analyzer that detects issues based on predefined rules.
"""
import re
from typing import List, Dict
from .utils import safe_split_lines

class CodeAnalyzer:
    def __init__(self, rules: Dict):
        self.rules = rules
    
    def analyze_line(self, line: str, line_number: int) -> List[Dict]:
        """Analyze a single line of code for issues."""
        try:
            issues = []
            for rule_name, rule in self.rules.items():
                if re.search(rule['pattern'], line):
                    issues.append({
                        'line': line_number,
                        'rule': rule_name,
                        'message': rule['message'],
                        'text': line.rstrip('\n\r')
                    })
            return issues
        except Exception as e:
            print(f"Warning: Error analyzing line {line_number}: {str(e)}")
            return []
    
    def analyze_code(self, content: str) -> List[Dict]:
        """Analyze code content for issues."""
        issues = []
        lines = safe_split_lines(content)
        
        for i, line in enumerate(lines, 1):
            line_issues = self.analyze_line(line, i)
            issues.extend(line_issues)
            
        return issues