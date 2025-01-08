from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Text
from .base import BaseMethod


@dataclass(kw_only=True)
class GetStickerSetName(BaseMethod):
    """
    Returns name of a sticker set by its identifier
    """

    __type__: Literal["getStickerSetName"] = "getStickerSetName"
    __returning_type__ = Text

    set_id: int
    """Identifier of the sticker set"""
