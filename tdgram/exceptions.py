class TDGramError(Exception):
    """Base exception class for all errors raised by tdgram."""


class TDLibError(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message

    def __str__(self):
        return f"TDLib Error {self.code}: {self.message}"


class TDLibTimeout(Exception):
    """Raised when a request to the TDLib client times out."""
