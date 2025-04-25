# Validation Status:
# - Security Validation: Nestor [2025-04-24] ✅
# - Strategic Validation: Pulse [2025-04-24] ✅
# - Governance Validation: Agent-47 [2025-04-24] ✅


# logdoc/errors/logdoc_exceptions.py
class LogdocError(Exception):
    def __init__(self, message, package="logdoc", module="unknown"):
        super().__init__(f"[{package}::{module}] {message}")

class HeaderInjectionError(LogdocError):
    def __init__(self, filepath, reason):
        super().__init__(
            f"Failed to inject header into {filepath}. Reason: {reason}",
            module="header_injector"
        )