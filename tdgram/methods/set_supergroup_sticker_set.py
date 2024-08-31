from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetSupergroupStickerSet(BaseMethod):
    """
    Changes the sticker set of a supergroup; requires can_change_info administrator right
    """

    __type__: Literal["setSupergroupStickerSet"] = "setSupergroupStickerSet"
    __returning_type__ = Ok

    supergroup_id: int
    """Identifier of the supergroup"""
    sticker_set_id: int
    """New value of the supergroup sticker set identifier. Use 0 to remove the supergroup sticker set"""
