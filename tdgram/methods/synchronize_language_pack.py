from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SynchronizeLanguagePack(BaseMethod):
    """
    Fetches the latest versions of all strings from a language pack in the current localization target from the server.
    """

    __type__: Literal["synchronizeLanguagePack"] = "synchronizeLanguagePack"
    __returning_type__ = Ok

    language_pack_id: str
    """Language pack identifier"""
