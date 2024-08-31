from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StoryListArchive(BaseType):
    """
    The list of stories, shown in the Arvhive chat list
    """

    __type__: Literal["storyListArchive"] = "storyListArchive"
