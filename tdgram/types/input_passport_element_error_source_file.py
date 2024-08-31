from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputPassportElementErrorSourceFile(BaseType):
    """
    The file contains an error. The error is considered resolved when the file changes
    """

    __type__: Literal["inputPassportElementErrorSourceFile"] = (
        "inputPassportElementErrorSourceFile"
    )

    file_hash: bytes
    """Current hash of the file which has the error"""
