"""
Main entry point for the code fixing system.
"""
from typing import Tuple, List
from .core.analyzer import CodeAnalyzer
from .core.fixer import CodeFixer
from .core.errors import CodeFixerError
from .core.issue import CodeIssue
from .core.validation import validate_code_input
from .core.logging import setup_logging, log_error
from .rules.style_rules import STYLE_RULES

def fix_code(code: str) -> Tuple[str, List[CodeIssue]]:
    """
    Fix code and return the fixed code along with a list of applied fixes.
    
    Args:
        code: Source code to analyze and fix
        
    Returns:
        Tuple containing:
            - Fixed code as string
            - List of CodeIssue objects describing found issues
            
    Raises:
        CodeFixerError: If analysis or fixing fails
    """
    setup_logging()
    
    try:
        validate_code_input(code)
        
        analyzer = CodeAnalyzer(STYLE_RULES)
        fixer = CodeFixer(STYLE_RULES)
        
        issues = analyzer.analyze_code(code)
        fixed_code = fixer.fix_code(code)
        
        return fixed_code, issues
    except CodeFixerError as e:
        log_error(e, "Code fixer error")
        return code, []
    except Exception as e:
        log_error(e, "Unexpected error")
        return code, []