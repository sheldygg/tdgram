from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class LinkPreviewTypeStory(BaseType):
    """
    The link is a link to a story. Link preview description is unavailable
    """

    __type__: Literal["linkPreviewTypeStory"] = "linkPreviewTypeStory"

    story_sender_chat_id: int
    """The identifier of the chat that posted the story"""
    story_id: int
    """Story identifier"""
