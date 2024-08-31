from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputFile


@dataclass(kw_only=True)
class InputThumbnail(BaseType):
    """
    A thumbnail to be sent along with a file; must be in JPEG or WEBP format for stickers, and less than 200 KB in size
    """

    __type__: Literal["inputThumbnail"] = "inputThumbnail"

    thumbnail: InputFile
    """Thumbnail file to send. Sending thumbnails by file_id is currently not supported"""
    width: int
    """Thumbnail width, usually shouldn't exceed 320. Use 0 if unknown"""
    height: int
    """Thumbnail height, usually shouldn't exceed 320. Use 0 if unknown"""
