from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class OpenStory(BaseMethod):
    """
    Informs TDLib that a story is opened and is being viewed by the user
    """

    __type__: Literal["openStory"] = "openStory"
    __returning_type__ = Ok

    story_sender_chat_id: int
    """The identifier of the sender of the opened story"""
    story_id: int
    """The identifier of the story"""
