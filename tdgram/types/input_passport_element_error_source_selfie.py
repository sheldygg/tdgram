from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputPassportElementErrorSourceSelfie(BaseType):
    """
    The selfie contains an error. The error is considered resolved when the file with the selfie changes
    """

    __type__: Literal["inputPassportElementErrorSourceSelfie"] = (
        "inputPassportElementErrorSourceSelfie"
    )

    file_hash: bytes
    """Current hash of the file containing the selfie"""
