from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PassportElementErrorSourceTranslationFile(BaseType):
    """
    One of files with the translation of the document contains an error. The error will be considered resolved when the file changes
    """

    __type__: Literal["passportElementErrorSourceTranslationFile"] = (
        "passportElementErrorSourceTranslationFile"
    )

    file_index: int
    """Index of a file with the error"""
