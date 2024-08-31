from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StoryList


@dataclass(kw_only=True)
class UpdateStoryListChatCount(BaseType):
    """
    Number of chats in a story list has changed
    """

    __type__: Literal["updateStoryListChatCount"] = "updateStoryListChatCount"

    story_list: StoryList
    """The story list"""
    chat_count: int
    """Approximate total number of chats with active stories in the list"""
