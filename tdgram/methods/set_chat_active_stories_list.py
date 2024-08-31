from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, StoryList
from .base import BaseMethod


@dataclass(kw_only=True)
class SetChatActiveStoriesList(BaseMethod):
    """
    Changes story list in which stories from the chat are shown
    """

    __type__: Literal["setChatActiveStoriesList"] = "setChatActiveStoriesList"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat that posted stories"""
    story_list: StoryList
    """New list for active stories posted by the chat"""
