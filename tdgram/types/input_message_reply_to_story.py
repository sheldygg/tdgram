from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputMessageReplyToStory(BaseType):
    """
    Describes a story to be replied
    """

    __type__: Literal["inputMessageReplyToStory"] = "inputMessageReplyToStory"

    story_sender_chat_id: int
    """The identifier of the sender of the story. Currently, stories can be replied only in the sender's chat and channel stories can't be replied"""
    story_id: int
    """The identifier of the story"""
