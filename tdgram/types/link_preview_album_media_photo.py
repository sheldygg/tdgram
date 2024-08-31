from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Photo


@dataclass(kw_only=True)
class LinkPreviewAlbumMediaPhoto(BaseType):
    """
    The media is a photo
    """

    __type__: Literal["linkPreviewAlbumMediaPhoto"] = "linkPreviewAlbumMediaPhoto"

    photo: Photo
    """Photo description"""
