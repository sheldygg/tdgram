from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import LanguagePackString, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetCustomLanguagePackString(BaseMethod):
    """
    Adds, edits or deletes a string in a custom local language pack. Can be called before authorization
    """

    __type__: Literal["setCustomLanguagePackString"] = "setCustomLanguagePackString"
    __returning_type__ = Ok

    language_pack_id: str
    """Identifier of a previously added custom local language pack in the current localization target"""
    new_string: LanguagePackString
    """New language pack string"""
