from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StoryVideo


@dataclass(kw_only=True)
class StoryContentVideo(BaseType):
    """
    A video story
    """

    __type__: Literal["storyContentVideo"] = "storyContentVideo"

    video: StoryVideo
    """The video in MPEG4 format"""
    alternative_video: StoryVideo | None = None
    """Alternative version of the video in MPEG4 format, encoded by x264 codec; may be null"""
