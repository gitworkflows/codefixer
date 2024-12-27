"""
Logging configuration and utilities.
"""
import logging
from typing import Optional

logger = logging.getLogger(__name__)

def setup_logging(level: int = logging.INFO) -> None:
    """Configure logging for the code fixer."""
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def log_error(error: Exception, context: Optional[str] = None) -> None:
    """Log an error with optional context."""
    message = f"{context}: {str(error)}" if context else str(error)
    logger.error(message)