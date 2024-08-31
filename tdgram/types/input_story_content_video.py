from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputFile


@dataclass(kw_only=True)
class InputStoryContentVideo(BaseType):
    """
    A video story
    """

    __type__: Literal["inputStoryContentVideo"] = "inputStoryContentVideo"

    video: InputFile
    """Video to be sent. The video size must be 720x1280. The video must be streamable and stored in MPEG4 format, after encoding with x265 codec and key frames added each second"""
    added_sticker_file_ids: list[int]
    """File identifiers of the stickers added to the video, if applicable"""
    duration: float
    """Precise duration of the video, in seconds; 0-60"""
    cover_frame_timestamp: float
    """Timestamp of the frame, which will be used as video thumbnail"""
    is_animation: bool
    """True, if the video has no sound"""
