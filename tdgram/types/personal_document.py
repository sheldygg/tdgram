from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import DatedFile


@dataclass(kw_only=True)
class PersonalDocument(BaseType):
    """
    A personal document, containing some information about a user
    """

    __type__: Literal["personalDocument"] = "personalDocument"

    files: list[DatedFile]
    """List of files containing the pages of the document"""
    translation: list[DatedFile]
    """List of files containing a certified English translation of the document"""
