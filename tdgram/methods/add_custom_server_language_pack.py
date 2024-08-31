from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class AddCustomServerLanguagePack(BaseMethod):
    """
    Adds a custom server language pack to the list of installed language packs in current localization target. Can be called before authorization
    """

    __type__: Literal["addCustomServerLanguagePack"] = "addCustomServerLanguagePack"
    __returning_type__ = Ok

    language_pack_id: str
    """Identifier of a language pack to be added"""
