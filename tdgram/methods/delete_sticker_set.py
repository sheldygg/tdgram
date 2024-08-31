from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteStickerSet(BaseMethod):
    """
    Completely deletes a sticker set
    """

    __type__: Literal["deleteStickerSet"] = "deleteStickerSet"
    __returning_type__ = Ok

    name: str
    """Sticker set name. The sticker set must be owned by the current user"""
