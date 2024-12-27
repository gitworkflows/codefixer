"""
Base classes for code fixing components.
"""
from abc import ABC, abstractmethod
from typing import Dict, List
from .issue import CodeIssue

class BaseAnalyzer(ABC):
    """Base class for code analyzers."""
    
    @abstractmethod
    def analyze_line(self, line: str, line_number: int) -> List[CodeIssue]:
        """Analyze a single line of code."""
        pass
    
    @abstractmethod
    def analyze_code(self, content: str) -> List[CodeIssue]:
        """Analyze entire code content."""
        pass

class BaseFixer(ABC):
    """Base class for code fixers."""
    
    @abstractmethod
    def fix_line(self, line: str) -> str:
        """Fix a single line of code."""
        pass
    
    @abstractmethod
    def fix_code(self, content: str) -> str:
        """Fix entire code content."""
        pass