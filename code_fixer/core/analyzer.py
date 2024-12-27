"""
Code analyzer that detects issues based on predefined rules.
"""
import re
from typing import List, Dict
from .base import BaseAnalyzer
from .errors import AnalysisError
from .issue import CodeIssue
from ..utils.text import safe_split_lines

class CodeAnalyzer(BaseAnalyzer):
    def __init__(self, rules: Dict):
        self.rules = rules
    
    def analyze_line(self, line: str, line_number: int) -> List[CodeIssue]:
        """Analyze a single line of code for issues."""
        try:
            issues = []
            for rule_name, rule in self.rules.items():
                if re.search(rule['pattern'], line):
                    issues.append(CodeIssue(
                        line=line_number,
                        rule=rule_name,
                        message=rule['message'],
                        text=line.rstrip('\n\r')
                    ))
            return issues
        except Exception as e:
            raise AnalysisError(f"Error analyzing line {line_number}: {str(e)}")
    
    def analyze_code(self, content: str) -> List[CodeIssue]:
        """Analyze code content for issues."""
        try:
            issues = []
            lines = safe_split_lines(content)
            
            for i, line in enumerate(lines, 1):
                line_issues = self.analyze_line(line, i)
                issues.extend(line_issues)
                
            return issues
        except Exception as e:
            raise AnalysisError(f"Error analyzing code: {str(e)}")