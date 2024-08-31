from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import File


@dataclass(kw_only=True)
class PhotoSize(BaseType):
    """
    Describes an image in JPEG format
    """

    __type__: Literal["photoSize"] = "photoSize"

    type: str
    """Image type (see https://core.telegram.org/constructor/photoSize)"""
    photo: File
    """Information about the image file"""
    width: int
    """Image width"""
    height: int
    """Image height"""
    progressive_sizes: list[int]
    """Sizes of progressive JPEG file prefixes, which can be used to preliminarily show the image; in bytes"""
