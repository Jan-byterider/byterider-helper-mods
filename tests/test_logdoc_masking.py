"""
Filename: test_logdoc_masking.py
"""

import json
from logdoc.logger import log_event, configure_logger
from pathlib import Path
import os

def test_log_event_masks_sensitive_fields(tmp_path):
    """
    Test that sensitive fields are masked when using log_event.
    """
    log_file = tmp_path / "test_log.json"
    logger = configure_logger(str(log_file))

    context = {
        "email": "user@example.com",
        "password": "SuperSecretPassword123!",
        "api_key": "sk-test-abcdef123456",
        "normal_data": "VisibleValue"
    }

    log_event(action="Test Action", context=context, logger=logger)

    with open(log_file, 'r') as f:
        lines = f.readlines()

    assert len(lines) == 1, "There should be exactly one log entry."

    log_entry = json.loads(lines[0])

    assert log_entry["action"] == "Test Action"
    assert log_entry["context"]["email"] == "user@example.com"
    assert log_entry["context"]["normal_data"] == "VisibleValue"
    assert log_entry["context"]["password"] == "[HIDDEN]"
    assert log_entry["context"]["api_key"] == "[HIDDEN]"
