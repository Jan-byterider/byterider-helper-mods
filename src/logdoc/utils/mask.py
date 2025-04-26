"""
Filename: mask.py
Author: Jan Janssens
Creation date: 2025-04-26
Last modified by: Nestor
Validated by: Jan Janssens
Last modified date: 2025-04-26
Repository: Public Git (ByteNestDAO - logdoc package)
"""

SENSITIVE_KEYS = ["password", "key", "token", "secret", "private"]

def mask_sensitive_data(data: dict) -> dict:
    """
    Mask sensitive information inside a dictionary.

    Args:
        data (dict): Dictionary containing variables to log.

    Returns:
        dict: New dictionary with sensitive fields replaced by [HIDDEN].
    """
    masked_data = {}
    for k, v in data.items():
        if any(sensitive_word in k.lower() for sensitive_word in SENSITIVE_KEYS):
            masked_data[k] = "[HIDDEN]"
        else:
            masked_data[k] = v
    return masked_data

