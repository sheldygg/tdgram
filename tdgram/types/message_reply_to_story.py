from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageReplyToStory(BaseType):
    """
    Describes a story replied by a given message
    """

    __type__: Literal["messageReplyToStory"] = "messageReplyToStory"

    story_sender_chat_id: int
    """The identifier of the sender of the story"""
    story_id: int
    """The identifier of the story"""
