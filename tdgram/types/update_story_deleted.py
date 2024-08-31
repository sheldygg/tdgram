from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateStoryDeleted(BaseType):
    """
    A story became inaccessible
    """

    __type__: Literal["updateStoryDeleted"] = "updateStoryDeleted"

    story_sender_chat_id: int
    """Identifier of the chat that posted the story"""
    story_id: int
    """Story identifier"""
