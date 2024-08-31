from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import EmojiStatus, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetChatEmojiStatus(BaseMethod):
    """
    Changes the emoji status of a chat. Use chatBoostLevelFeatures.can_set_emoji_status to check whether an emoji status can be set. Requires can_change_info administrator right
    """

    __type__: Literal["setChatEmojiStatus"] = "setChatEmojiStatus"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    emoji_status: EmojiStatus | None = None
    """New emoji status; pass null to remove emoji status"""
