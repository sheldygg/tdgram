from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText, InputFile, InputThumbnail


@dataclass(kw_only=True)
class InputMessageAudio(BaseType):
    """
    An audio message
    """

    __type__: Literal["inputMessageAudio"] = "inputMessageAudio"

    audio: InputFile
    """Audio file to be sent"""
    album_cover_thumbnail: InputThumbnail | None = None
    """Thumbnail of the cover for the album; pass null to skip thumbnail uploading"""
    duration: int
    """Duration of the audio, in seconds; may be replaced by the server"""
    title: str
    """Title of the audio; 0-64 characters; may be replaced by the server"""
    performer: str
    """Performer of the audio; 0-64 characters, may be replaced by the server"""
    caption: FormattedText | None = None
    """Audio caption; pass null to use an empty caption; 0-getOption('message_caption_length_max') characters"""
