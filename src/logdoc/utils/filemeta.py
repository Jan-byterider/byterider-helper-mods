# Validation Status:
# - Security Validation: Nestor [2025-04-24] ✅
# - Strategic Validation: Pulse [2025-04-24] ✅
# - Governance Validation: Agent-47 [2025-04-24] ✅


# logdoc/utils/filemeta.py
import os
from datetime import datetime

def get_file_metadata(path):
    stats = os.stat(path)
    return {
        "created": datetime.fromtimestamp(stats.st_ctime),
        "modified": datetime.fromtimestamp(stats.st_mtime)
    }