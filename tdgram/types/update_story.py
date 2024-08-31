from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Story


@dataclass(kw_only=True)
class UpdateStory(BaseType):
    """
    A story was changed
    """

    __type__: Literal["updateStory"] = "updateStory"

    story: Story
    """The new information about the story"""
