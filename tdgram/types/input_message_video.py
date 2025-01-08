from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText, InputFile, InputThumbnail, MessageSelfDestructType


@dataclass(kw_only=True)
class InputMessageVideo(BaseType):
    """
    A video message
    """

    __type__: Literal["inputMessageVideo"] = "inputMessageVideo"

    video: InputFile
    """Video to be sent. The video is expected to be re-encoded to MPEG4 format with H.264 codec by the sender"""
    thumbnail: InputThumbnail | None = None
    """Video thumbnail; pass null to skip thumbnail uploading"""
    added_sticker_file_ids: list[int]
    """File identifiers of the stickers added to the video, if applicable"""
    duration: int
    """Duration of the video, in seconds"""
    width: int
    """Video width"""
    height: int
    """Video height"""
    supports_streaming: bool
    """True, if the video is expected to be streamed"""
    caption: FormattedText | None = None
    """Video caption; pass null to use an empty caption; 0-getOption('message_caption_length_max') characters"""
    show_caption_above_media: bool
    """True, if the caption must be shown above the video; otherwise, the caption must be shown below the video; not supported in secret chats"""
    self_destruct_type: MessageSelfDestructType | None = None
    """Video self-destruct type; pass null if none; private chats only"""
    has_spoiler: bool
    """True, if the video preview must be covered by a spoiler animation; not supported in secret chats"""
