"""
Constants and configuration for the code fixing system.
"""

# Rule definitions
STYLE_RULES = {
    'trailing_whitespace': {
        'pattern': r'[ \t]+$',
        'fix': '',
        'message': 'Remove trailing whitespace'
    },
    'multiple_blank_lines': {
        'pattern': r'\n\n\n+',
        'fix': '\n\n',
        'message': 'Multiple blank lines should be replaced with a single blank line'
    },
    'mutable_default_args': {
        'pattern': r'def \w+\((.*?)\s*=\s*\[\]|(.*?)\s*=\s*{}\)',
        'fix': None,  # Complex fix, handled separately
        'message': 'Mutable default arguments should be replaced with None'
    },
    'invalid_variable_name': {
        'pattern': r'\b[A-Z][a-z]*\s*=',
        'fix': None,  # Complex fix, handled separately
        'message': 'Variable names should be lowercase with underscores'
    }
}