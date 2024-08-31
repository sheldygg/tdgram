from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatActiveStories


@dataclass(kw_only=True)
class UpdateChatActiveStories(BaseType):
    """
    The list of active stories posted by a specific chat has changed
    """

    __type__: Literal["updateChatActiveStories"] = "updateChatActiveStories"

    active_stories: ChatActiveStories
    """The new list of active stories"""
