from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText, InputFile, InputThumbnail


@dataclass(kw_only=True)
class InputMessageAnimation(BaseType):
    """
    An animation message (GIF-style).
    """

    __type__: Literal["inputMessageAnimation"] = "inputMessageAnimation"

    animation: InputFile
    """Animation file to be sent"""
    thumbnail: InputThumbnail | None = None
    """Animation thumbnail; pass null to skip thumbnail uploading"""
    added_sticker_file_ids: list[int]
    """File identifiers of the stickers added to the animation, if applicable"""
    duration: int
    """Duration of the animation, in seconds"""
    width: int
    """Width of the animation; may be replaced by the server"""
    height: int
    """Height of the animation; may be replaced by the server"""
    caption: FormattedText | None = None
    """Animation caption; pass null to use an empty caption; 0-getOption('message_caption_length_max') characters"""
    show_caption_above_media: bool
    """True, if the caption must be shown above the animation; otherwise, the caption must be shown below the animation; not supported in secret chats"""
    has_spoiler: bool
    """True, if the animation preview must be covered by a spoiler animation; not supported in secret chats"""
