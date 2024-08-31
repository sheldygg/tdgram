from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleStoryIsPostedToChatPage(BaseMethod):
    """
    Toggles whether a story is accessible after expiration. Can be called only if story.can_toggle_is_posted_to_chat_page == true
    """

    __type__: Literal["toggleStoryIsPostedToChatPage"] = "toggleStoryIsPostedToChatPage"
    __returning_type__ = Ok

    story_sender_chat_id: int
    """Identifier of the chat that posted the story"""
    story_id: int
    """Identifier of the story"""
    is_posted_to_chat_page: bool
    """Pass true to make the story accessible after expiration; pass false to make it private"""
