from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetChatPinnedStories(BaseMethod):
    """
    Changes the list of pinned stories on a chat page; requires can_edit_stories right in the chat
    """

    __type__: Literal["setChatPinnedStories"] = "setChatPinnedStories"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat that posted the stories"""
    story_ids: list[int]
    """New list of pinned stories. All stories must be posted to the chat page first. There can be up to getOption('pinned_story_count_max') pinned stories on a chat page"""
