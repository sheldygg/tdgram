from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PassportElementErrorSourceTranslationFiles(BaseType):
    """
    The translation of the document contains an error. The error will be considered resolved when the list of translation files changes
    """

    __type__: Literal["passportElementErrorSourceTranslationFiles"] = (
        "passportElementErrorSourceTranslationFiles"
    )
