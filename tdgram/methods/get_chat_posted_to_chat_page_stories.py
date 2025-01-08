from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Stories
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatPostedToChatPageStories(BaseMethod):
    """
    Returns the list of stories that posted by the given chat to its chat page. If from_story_id == 0, then pinned stories are returned first.
    """

    __type__: Literal["getChatPostedToChatPageStories"] = "getChatPostedToChatPageStories"
    __returning_type__ = Stories

    chat_id: int
    """Chat identifier"""
    from_story_id: int
    """Identifier of the story starting from which stories must be returned; use 0 to get results from pinned and the newest story"""
    limit: int
    """The maximum number of stories to be returned."""
