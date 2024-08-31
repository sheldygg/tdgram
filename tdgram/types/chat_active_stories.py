from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StoryInfo, StoryList


@dataclass(kw_only=True)
class ChatActiveStories(BaseType):
    """
    Describes active stories posted by a chat
    """

    __type__: Literal["chatActiveStories"] = "chatActiveStories"

    chat_id: int
    """Identifier of the chat that posted the stories"""
    list: StoryList | None = None
    """Identifier of the story list in which the stories are shown; may be null if the stories aren't shown in a story list"""
    order: int
    """A parameter used to determine order of the stories in the story list; 0 if the stories doesn't need to be shown in the story list. Stories must be sorted by the pair (order, story_sender_chat_id) in descending order"""
    max_read_story_id: int
    """Identifier of the last read active story"""
    stories: list[StoryInfo]
    """Basic information about the stories; use getStory to get full information about the stories. The stories are in chronological order (i.e., in order of increasing story identifiers)"""
