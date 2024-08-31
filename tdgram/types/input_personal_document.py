from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputFile


@dataclass(kw_only=True)
class InputPersonalDocument(BaseType):
    """
    A personal document to be saved to Telegram Passport
    """

    __type__: Literal["inputPersonalDocument"] = "inputPersonalDocument"

    files: list[InputFile]
    """List of files containing the pages of the document"""
    translation: list[InputFile]
    """List of files containing a certified English translation of the document"""
