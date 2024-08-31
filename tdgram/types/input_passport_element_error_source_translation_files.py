from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputPassportElementErrorSourceTranslationFiles(BaseType):
    """
    The translation of the document contains an error. The error is considered resolved when the list of files changes
    """

    __type__: Literal["inputPassportElementErrorSourceTranslationFiles"] = (
        "inputPassportElementErrorSourceTranslationFiles"
    )

    file_hashes: list[bytes]
    """Current hashes of all files with the translation"""
