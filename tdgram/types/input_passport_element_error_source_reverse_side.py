from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputPassportElementErrorSourceReverseSide(BaseType):
    """
    The reverse side of the document contains an error. The error is considered resolved when the file with the reverse side of the document changes
    """

    __type__: Literal["inputPassportElementErrorSourceReverseSide"] = (
        "inputPassportElementErrorSourceReverseSide"
    )

    file_hash: bytes
    """Current hash of the file containing the reverse side"""
