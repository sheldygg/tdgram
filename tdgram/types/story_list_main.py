from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StoryListMain(BaseType):
    """
    The list of stories, shown in the main chat list and folder chat lists
    """

    __type__: Literal["storyListMain"] = "storyListMain"
