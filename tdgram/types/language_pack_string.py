from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import LanguagePackStringValue


@dataclass(kw_only=True)
class LanguagePackString(BaseType):
    """
    Represents one language pack string
    """

    __type__: Literal["languagePackString"] = "languagePackString"

    key: str
    """String key"""
    value: LanguagePackStringValue | None = None
    """String value; pass null if the string needs to be taken from the built-in English language pack"""
