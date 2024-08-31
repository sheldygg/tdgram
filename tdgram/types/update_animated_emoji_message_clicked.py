from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Sticker


@dataclass(kw_only=True)
class UpdateAnimatedEmojiMessageClicked(BaseType):
    """
    Some animated emoji message was clicked and a big animated sticker must be played if the message is visible on the screen. chatActionWatchingAnimations with the text of the message needs to be sent if the sticker is played
    """

    __type__: Literal["updateAnimatedEmojiMessageClicked"] = "updateAnimatedEmojiMessageClicked"

    chat_id: int
    """Chat identifier"""
    message_id: int
    """Message identifier"""
    sticker: Sticker
    """The animated sticker to be played"""
