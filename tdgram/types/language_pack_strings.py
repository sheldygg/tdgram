from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import LanguagePackString


@dataclass(kw_only=True)
class LanguagePackStrings(BaseType):
    """
    Contains a list of language pack strings
    """

    __type__: Literal["languagePackStrings"] = "languagePackStrings"

    strings: list[LanguagePackString]
    """A list of language pack strings"""
