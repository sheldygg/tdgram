from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText, InputFile, InputThumbnail, MessageSelfDestructType


@dataclass(kw_only=True)
class InputMessagePhoto(BaseType):
    """
    A photo message
    """

    __type__: Literal["inputMessagePhoto"] = "inputMessagePhoto"

    photo: InputFile
    """Photo to send. The photo must be at most 10 MB in size. The photo's width and height must not exceed 10000 in total. Width and height ratio must be at most 20"""
    thumbnail: InputThumbnail | None = None
    """Photo thumbnail to be sent; pass null to skip thumbnail uploading. The thumbnail is sent to the other party only in secret chats"""
    added_sticker_file_ids: list[int]
    """File identifiers of the stickers added to the photo, if applicable"""
    width: int
    """Photo width"""
    height: int
    """Photo height"""
    caption: FormattedText | None = None
    """Photo caption; pass null to use an empty caption; 0-getOption('message_caption_length_max') characters"""
    show_caption_above_media: bool
    """True, if the caption must be shown above the photo; otherwise, the caption must be shown below the photo; not supported in secret chats"""
    self_destruct_type: MessageSelfDestructType | None = None
    """Photo self-destruct type; pass null if none; private chats only"""
    has_spoiler: bool
    """True, if the photo preview must be covered by a spoiler animation; not supported in secret chats"""
