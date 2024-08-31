from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputPassportElementErrorSourceFrontSide(BaseType):
    """
    The front side of the document contains an error. The error is considered resolved when the file with the front side of the document changes
    """

    __type__: Literal["inputPassportElementErrorSourceFrontSide"] = (
        "inputPassportElementErrorSourceFrontSide"
    )

    file_hash: bytes
    """Current hash of the file containing the front side"""
