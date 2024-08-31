from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StoryOrigin


@dataclass(kw_only=True)
class StoryRepostInfo(BaseType):
    """
    Contains information about original story that was reposted
    """

    __type__: Literal["storyRepostInfo"] = "storyRepostInfo"

    origin: StoryOrigin
    """Origin of the story that was reposted"""
    is_content_modified: bool
    """True, if story content was modified during reposting; otherwise, story wasn't modified"""
