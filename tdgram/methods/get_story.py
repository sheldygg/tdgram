from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Story
from .base import BaseMethod


@dataclass(kw_only=True)
class GetStory(BaseMethod):
    """
    Returns a story
    """

    __type__: Literal["getStory"] = "getStory"
    __returning_type__ = Story

    story_sender_chat_id: int
    """Identifier of the chat that posted the story"""
    story_id: int
    """Story identifier"""
    only_local: bool
    """Pass true to get only locally available information without sending network requests"""
