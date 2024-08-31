from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class EditStoryCover(BaseMethod):
    """
    Changes cover of a video story. Can be called only if story.can_be_edited == true and the story isn't being edited now
    """

    __type__: Literal["editStoryCover"] = "editStoryCover"
    __returning_type__ = Ok

    story_sender_chat_id: int
    """Identifier of the chat that posted the story"""
    story_id: int
    """Identifier of the story to edit"""
    cover_frame_timestamp: float
    """New timestamp of the frame, which will be used as video thumbnail"""
