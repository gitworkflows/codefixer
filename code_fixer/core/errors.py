"""
Custom exceptions for the code fixing system.
"""

class CodeFixerError(Exception):
    """Base exception for code fixer errors."""
    pass

class AnalysisError(CodeFixerError):
    """Raised when code analysis fails."""
    pass

class FixerError(CodeFixerError):
    """Raised when code fixing fails."""
    pass

class ValidationError(CodeFixerError):
    """Raised when input validation fails."""
    pass

class CompilationError(CodeFixerError):
    """Raised when code compilation fails."""
    pass