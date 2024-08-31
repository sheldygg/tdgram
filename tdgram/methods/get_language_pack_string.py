from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import LanguagePackStringValue
from .base import BaseMethod


@dataclass(kw_only=True)
class GetLanguagePackString(BaseMethod):
    """
    Returns a string stored in the local database from the specified localization target and language pack by its key. Returns a 404 error if the string is not found. Can be called synchronously
    """

    __type__: Literal["getLanguagePackString"] = "getLanguagePackString"
    __returning_type__ = LanguagePackStringValue

    language_pack_database_path: str
    """Path to the language pack database in which strings are stored"""
    localization_target: str
    """Localization target to which the language pack belongs"""
    language_pack_id: str
    """Language pack identifier"""
    key: str
    """Language pack key of the string to be returned"""
