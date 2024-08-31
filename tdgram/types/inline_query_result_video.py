from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Video


@dataclass(kw_only=True)
class InlineQueryResultVideo(BaseType):
    """
    Represents a video
    """

    __type__: Literal["inlineQueryResultVideo"] = "inlineQueryResultVideo"

    id: str
    """Unique identifier of the query result"""
    video: Video
    """Video"""
    title: str
    """Title of the video"""
    description: str
    """Description of the video"""
