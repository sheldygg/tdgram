from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import LanguagePackInfo, LanguagePackString, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetCustomLanguagePack(BaseMethod):
    """
    Adds or changes a custom local language pack to the current localization target
    """

    __type__: Literal["setCustomLanguagePack"] = "setCustomLanguagePack"
    __returning_type__ = Ok

    info: LanguagePackInfo
    """Information about the language pack. Language pack identifier must start with 'X', consist only of English letters, digits and hyphens, and must not exceed 64 characters. Can be called before authorization"""
    strings: list[LanguagePackString]
    """Strings of the new language pack"""
