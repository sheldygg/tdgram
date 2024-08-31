from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FormattedText, InputStoryAreas, InputStoryContent, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class EditStory(BaseMethod):
    """
    Changes content and caption of a story. Can be called only if story.can_be_edited == true
    """

    __type__: Literal["editStory"] = "editStory"
    __returning_type__ = Ok

    story_sender_chat_id: int
    """Identifier of the chat that posted the story"""
    story_id: int
    """Identifier of the story to edit"""
    content: InputStoryContent | None = None
    """New content of the story; pass null to keep the current content"""
    areas: InputStoryAreas | None = None
    """New clickable rectangle areas to be shown on the story media; pass null to keep the current areas. Areas can't be edited if story content isn't changed"""
    caption: FormattedText | None = None
    """New story caption; pass null to keep the current caption"""
