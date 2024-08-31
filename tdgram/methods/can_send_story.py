from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import CanSendStoryResult
from .base import BaseMethod


@dataclass(kw_only=True)
class CanSendStory(BaseMethod):
    """
    Checks whether the current user can send a story on behalf of a chat; requires can_post_stories right for supergroup and channel chats
    """

    __type__: Literal["canSendStory"] = "canSendStory"
    __returning_type__ = CanSendStoryResult

    chat_id: int
    """Chat identifier. Pass Saved Messages chat identifier when posting a story on behalf of the current user"""
