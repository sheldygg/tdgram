from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import LanguagePackStrings
from .base import BaseMethod


@dataclass(kw_only=True)
class GetLanguagePackStrings(BaseMethod):
    """
    Returns strings from a language pack in the current localization target by their keys. Can be called before authorization
    """

    __type__: Literal["getLanguagePackStrings"] = "getLanguagePackStrings"
    __returning_type__ = LanguagePackStrings

    language_pack_id: str
    """Language pack identifier of the strings to be returned"""
    keys: list[str]
    """Language pack keys of the strings to be returned; leave empty to request all available strings"""
