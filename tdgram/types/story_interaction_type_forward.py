from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Message


@dataclass(kw_only=True)
class StoryInteractionTypeForward(BaseType):
    """
    A forward of the story as a message
    """

    __type__: Literal["storyInteractionTypeForward"] = "storyInteractionTypeForward"

    message: Message
    """The message with story forward"""
