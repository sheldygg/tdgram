from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputPassportElementErrorSourceTranslationFile(BaseType):
    """
    One of the files containing the translation of the document contains an error. The error is considered resolved when the file with the translation changes
    """

    __type__: Literal["inputPassportElementErrorSourceTranslationFile"] = (
        "inputPassportElementErrorSourceTranslationFile"
    )

    file_hash: bytes
    """Current hash of the file containing the translation"""
