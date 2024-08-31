from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteStory(BaseMethod):
    """
    Deletes a previously sent story. Can be called only if story.can_be_deleted == true
    """

    __type__: Literal["deleteStory"] = "deleteStory"
    __returning_type__ = Ok

    story_sender_chat_id: int
    """Identifier of the chat that posted the story"""
    story_id: int
    """Identifier of the story to delete"""
