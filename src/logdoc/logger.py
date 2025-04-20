"""
Filename: logger.py
Author: Jan Janssens
Creation date: 2025-04-19
Last modified by: Nestor
Validated by: Jan Janssens
Last modified date: 2025-04-20
Repository: Public Git (ByteNestDAO - logdoc package)
"""

import json
import logging
from datetime import datetime, timezone

def configure_logger(log_file_path: str):
    """
    Configure logging to both file and stdout with JSON formatting.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(message)s')

    # File handler
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Avoid duplicate handlers
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

def log_event(action: str, context: dict = None):
    entry = {
        "timestamp": datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S"),
        "action": action,
        "context": context or {}
    }
    logging.info(json.dumps(entry))
