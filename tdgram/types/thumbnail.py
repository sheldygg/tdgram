from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import File, ThumbnailFormat


@dataclass(kw_only=True)
class Thumbnail(BaseType):
    """
    Represents a thumbnail
    """

    __type__: Literal["thumbnail"] = "thumbnail"

    format: ThumbnailFormat
    """Thumbnail format"""
    width: int
    """Thumbnail width"""
    height: int
    """Thumbnail height"""
    file: File
    """The thumbnail"""
