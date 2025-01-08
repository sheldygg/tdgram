from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import File


@dataclass(kw_only=True)
class AlternativeVideo(BaseType):
    """
    Describes an alternative re-encoded quality of a video file
    """

    __type__: Literal["alternativeVideo"] = "alternativeVideo"

    width: int
    """Video width"""
    height: int
    """Video height"""
    codec: str
    """Codec used for video file encoding, for example, 'h264', 'h265', or 'av1'"""
    hls_file: File
    """HLS file describing the video"""
    video: File
    """File containing the video"""
