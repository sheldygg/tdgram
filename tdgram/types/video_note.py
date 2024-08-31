from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import File, Minithumbnail, SpeechRecognitionResult, Thumbnail


@dataclass(kw_only=True)
class VideoNote(BaseType):
    """
    Describes a video note. The video must be equal in width and height, cropped to a circle, and stored in MPEG4 format
    """

    __type__: Literal["videoNote"] = "videoNote"

    duration: int
    """Duration of the video, in seconds; as defined by the sender"""
    waveform: bytes | None = None
    """A waveform representation of the video note's audio in 5-bit format; may be empty if unknown"""
    length: int
    """Video width and height; as defined by the sender"""
    minithumbnail: Minithumbnail | None = None
    """Video minithumbnail; may be null"""
    thumbnail: Thumbnail | None = None
    """Video thumbnail in JPEG format; as defined by the sender; may be null"""
    speech_recognition_result: SpeechRecognitionResult | None = None
    """Result of speech recognition in the video note; may be null"""
    video: File
    """File containing the video"""
