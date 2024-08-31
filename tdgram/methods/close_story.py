from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class CloseStory(BaseMethod):
    """
    Informs TDLib that a story is closed by the user
    """

    __type__: Literal["closeStory"] = "closeStory"
    __returning_type__ = Ok

    story_sender_chat_id: int
    """The identifier of the sender of the story to close"""
    story_id: int
    """The identifier of the story"""
