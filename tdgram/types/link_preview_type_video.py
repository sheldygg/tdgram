from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Video


@dataclass(kw_only=True)
class LinkPreviewTypeVideo(BaseType):
    """
    The link is a link to a video
    """

    __type__: Literal["linkPreviewTypeVideo"] = "linkPreviewTypeVideo"

    video: Video
    """The video description"""
