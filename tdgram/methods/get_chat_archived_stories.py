from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Stories
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatArchivedStories(BaseMethod):
    """
    Returns the list of all stories posted by the given chat; requires can_edit_stories right in the chat.
    """

    __type__: Literal["getChatArchivedStories"] = "getChatArchivedStories"
    __returning_type__ = Stories

    chat_id: int
    """Chat identifier"""
    from_story_id: int
    """Identifier of the story starting from which stories must be returned; use 0 to get results from the last story"""
    limit: int
    """The maximum number of stories to be returned."""
