from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class LanguagePackInfo(BaseType):
    """
    Contains information about a language pack
    """

    __type__: Literal["languagePackInfo"] = "languagePackInfo"

    id: str
    """Unique language pack identifier"""
    base_language_pack_id: str | None = None
    """Identifier of a base language pack; may be empty. If a string is missed in the language pack, then it must be fetched from base language pack. Unsupported in custom language packs"""
    name: str
    """Language name"""
    native_name: str
    """Name of the language in that language"""
    plural_code: str
    """A language code to be used to apply plural forms. See https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html for more information"""
    is_official: bool
    """True, if the language pack is official"""
    is_rtl: bool
    """True, if the language pack strings are RTL"""
    is_beta: bool
    """True, if the language pack is a beta language pack"""
    is_installed: bool
    """True, if the language pack is installed by the current user"""
    total_string_count: int
    """Total number of non-deleted strings from the language pack"""
    translated_string_count: int
    """Total number of translated strings from the language pack"""
    local_string_count: int
    """Total number of non-deleted strings from the language pack available locally"""
    translation_url: str
    """Link to language translation interface; empty for custom local language packs"""
