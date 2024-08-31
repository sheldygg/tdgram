from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageStory(BaseType):
    """
    A message with a forwarded story
    """

    __type__: Literal["messageStory"] = "messageStory"

    story_sender_chat_id: int
    """Identifier of the chat that posted the story"""
    story_id: int
    """Story identifier"""
    via_mention: bool
    """True, if the story was automatically forwarded because of a mention of the user"""
