"""
Filename: logger.py
Author: Jan Janssens
Creation date: 2025-04-19
Last modified by: Nestor
Validated by: Jan Janssens
Last modified date: 2025-04-26
Repository: Public Git (ByteNestDAO - logdoc package)
"""

import json
import logging
from datetime import datetime, timezone
from logdoc.utils.mask import mask_sensitive_data

def configure_logger(log_file_path: str):
    """
    Configure logging to both file and stdout with JSON formatting.
    """
    logger = logging.getLogger("scannest_logger")  #  use named logger
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(message)s')

    # Clear handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    # File handler
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger  #  return explicit logger object

def log_event(action: str, context: dict = None, logger=None):
    from logdoc.utils.mask import mask_sensitive_data

    if logger is None:
        logger = logging.getLogger("scannest_logger")

    masked_context = mask_sensitive_data(context or {})

    entry = {
        "timestamp": datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S"),
        "action": action,
        "context": masked_context
    }
    logger.info(json.dumps(entry))

    # Flush after logging
    for handler in logger.handlers:
        handler.flush()
