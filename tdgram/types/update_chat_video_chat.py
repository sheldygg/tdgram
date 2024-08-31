from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import VideoChat


@dataclass(kw_only=True)
class UpdateChatVideoChat(BaseType):
    """
    A chat video chat state has changed
    """

    __type__: Literal["updateChatVideoChat"] = "updateChatVideoChat"

    chat_id: int
    """Chat identifier"""
    video_chat: VideoChat
    """New value of video_chat"""
