"""
Regular expression patterns for code style rules.
"""

PATTERNS = {
    'trailing_whitespace': r'[ \t]+$',
    'multiple_blank_lines': r'\n\n\n+',
    'mutable_default_args': r'def \w+\((.*?)\s*=\s*\[\]|(.*?)\s*=\s*{}\)',
    'invalid_variable_name': r'\b[A-Z][a-z]*\s*='
}