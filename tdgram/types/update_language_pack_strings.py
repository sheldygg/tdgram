from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import LanguagePackString


@dataclass(kw_only=True)
class UpdateLanguagePackStrings(BaseType):
    """
    Some language pack strings have been updated
    """

    __type__: Literal["updateLanguagePackStrings"] = "updateLanguagePackStrings"

    localization_target: str
    """Localization target to which the language pack belongs"""
    language_pack_id: str
    """Identifier of the updated language pack"""
    strings: list[LanguagePackString]
    """List of changed language pack strings; empty if all strings have changed"""
