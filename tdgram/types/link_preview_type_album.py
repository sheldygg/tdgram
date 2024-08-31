from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import LinkPreviewAlbumMedia


@dataclass(kw_only=True)
class LinkPreviewTypeAlbum(BaseType):
    """
    The link is a link to a media album consisting of photos and videos
    """

    __type__: Literal["linkPreviewTypeAlbum"] = "linkPreviewTypeAlbum"

    media: list[LinkPreviewAlbumMedia]
    """The list of album media"""
    caption: str
    """Album caption"""
