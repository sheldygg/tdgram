from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import File, Minithumbnail, Thumbnail


@dataclass(kw_only=True)
class Audio(BaseType):
    """
    Describes an audio file. Audio is usually in MP3 or M4A format
    """

    __type__: Literal["audio"] = "audio"

    duration: int
    """Duration of the audio, in seconds; as defined by the sender"""
    title: str
    """Title of the audio; as defined by the sender"""
    performer: str
    """Performer of the audio; as defined by the sender"""
    file_name: str
    """Original name of the file; as defined by the sender"""
    mime_type: str
    """The MIME type of the file; as defined by the sender"""
    album_cover_minithumbnail: Minithumbnail | None = None
    """The minithumbnail of the album cover; may be null"""
    album_cover_thumbnail: Thumbnail | None = None
    """The thumbnail of the album cover in JPEG format; as defined by the sender. The full size thumbnail is supposed to be extracted from the downloaded audio file; may be null"""
    external_album_covers: list[Thumbnail]
    """Album cover variants to use if the downloaded audio file contains no album cover. Provided thumbnail dimensions are approximate"""
    audio: File
    """File containing the audio"""
