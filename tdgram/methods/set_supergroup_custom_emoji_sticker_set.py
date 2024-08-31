from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetSupergroupCustomEmojiStickerSet(BaseMethod):
    """
    Changes the custom emoji sticker set of a supergroup; requires can_change_info administrator right. The chat must have at least chatBoostFeatures.min_custom_emoji_sticker_set_boost_level boost level to pass the corresponding color
    """

    __type__: Literal["setSupergroupCustomEmojiStickerSet"] = "setSupergroupCustomEmojiStickerSet"
    __returning_type__ = Ok

    supergroup_id: int
    """Identifier of the supergroup"""
    custom_emoji_sticker_set_id: int
    """New value of the custom emoji sticker set identifier for the supergroup. Use 0 to remove the custom emoji sticker set in the supergroup"""
