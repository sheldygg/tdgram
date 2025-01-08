from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import AlternativeVideo, FormattedText, Video


@dataclass(kw_only=True)
class MessageVideo(BaseType):
    """
    A video message
    """

    __type__: Literal["messageVideo"] = "messageVideo"

    video: Video
    """The video description"""
    alternative_videos: list[AlternativeVideo]
    """Alternative qualities of the video"""
    caption: FormattedText
    """Video caption"""
    show_caption_above_media: bool
    """True, if the caption must be shown above the video; otherwise, the caption must be shown below the video"""
    has_spoiler: bool
    """True, if the video preview must be covered by a spoiler animation"""
    is_secret: bool
    """True, if the video thumbnail must be blurred and the video must be shown only while tapped"""
