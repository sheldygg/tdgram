from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ChangeStickerSet(BaseMethod):
    """
    Installs/uninstalls or activates/archives a sticker set
    """

    __type__: Literal["changeStickerSet"] = "changeStickerSet"
    __returning_type__ = Ok

    set_id: int
    """Identifier of the sticker set"""
    is_installed: bool
    """The new value of is_installed"""
    is_archived: bool
    """The new value of is_archived. A sticker set can't be installed and archived simultaneously"""
