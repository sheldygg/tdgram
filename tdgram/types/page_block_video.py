from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PageBlockCaption, Video


@dataclass(kw_only=True)
class PageBlockVideo(BaseType):
    """
    A video
    """

    __type__: Literal["pageBlockVideo"] = "pageBlockVideo"

    video: Video | None = None
    """Video file; may be null"""
    caption: PageBlockCaption
    """Video caption"""
    need_autoplay: bool
    """True, if the video must be played automatically"""
    is_looped: bool
    """True, if the video must be looped"""
