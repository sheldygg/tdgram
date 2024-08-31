from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteLanguagePack(BaseMethod):
    """
    Deletes all information about a language pack in the current localization target. The language pack which is currently in use (including base language pack) or is being synchronized can't be deleted.
    """

    __type__: Literal["deleteLanguagePack"] = "deleteLanguagePack"
    __returning_type__ = Ok

    language_pack_id: str
    """Identifier of the language pack to delete"""
