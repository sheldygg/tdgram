from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputFile, InputPaidMediaType, InputThumbnail


@dataclass(kw_only=True)
class InputPaidMedia(BaseType):
    """
    Describes a paid media to be sent
    """

    __type__: Literal["inputPaidMedia"] = "inputPaidMedia"

    type: InputPaidMediaType
    """Type of the media"""
    media: InputFile
    """Photo or video to be sent"""
    thumbnail: InputThumbnail | None = None
    """Media thumbnail; pass null to skip thumbnail uploading"""
    added_sticker_file_ids: list[int]
    """File identifiers of the stickers added to the media, if applicable"""
    width: int
    """Media width"""
    height: int
    """Media height"""
