"""
Style rules definitions combining patterns, messages and fixes.
"""
from typing import Dict
from .patterns import PATTERNS
from .messages import MESSAGES
from .fixes import FIXES
from .validators import validate_rule

def create_style_rules() -> Dict:
    """Create and validate style rules."""
    rules = {
        rule_name: {
            'pattern': PATTERNS[rule_name],
            'message': MESSAGES[rule_name],
            'fix': FIXES[rule_name]
        }
        for rule_name in PATTERNS.keys()
    }
    
    # Validate all rules
    for rule in rules.values():
        validate_rule(rule)
        
    return rules

STYLE_RULES = create_style_rules()