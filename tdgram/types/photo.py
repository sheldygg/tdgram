from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Minithumbnail, PhotoSize


@dataclass(kw_only=True)
class Photo(BaseType):
    """
    Describes a photo
    """

    __type__: Literal["photo"] = "photo"

    has_stickers: bool
    """True, if stickers were added to the photo. The list of corresponding sticker sets can be received using getAttachedStickerSets"""
    minithumbnail: Minithumbnail | None = None
    """Photo minithumbnail; may be null"""
    sizes: list[PhotoSize]
    """Available variants of the photo, in different sizes"""
