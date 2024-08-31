from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputPassportElementErrorSourceFiles(BaseType):
    """
    The list of attached files contains an error. The error is considered resolved when the file list changes
    """

    __type__: Literal["inputPassportElementErrorSourceFiles"] = (
        "inputPassportElementErrorSourceFiles"
    )

    file_hashes: list[bytes]
    """Current hashes of all attached files"""
