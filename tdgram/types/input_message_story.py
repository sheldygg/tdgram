from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputMessageStory(BaseType):
    """
    A message with a forwarded story. Stories can't be sent to secret chats. A story can be forwarded only if story.can_be_forwarded
    """

    __type__: Literal["inputMessageStory"] = "inputMessageStory"

    story_sender_chat_id: int
    """Identifier of the chat that posted the story"""
    story_id: int
    """Story identifier"""
