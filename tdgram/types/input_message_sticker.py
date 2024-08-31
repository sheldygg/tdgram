from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputFile, InputThumbnail


@dataclass(kw_only=True)
class InputMessageSticker(BaseType):
    """
    A sticker message
    """

    __type__: Literal["inputMessageSticker"] = "inputMessageSticker"

    sticker: InputFile
    """Sticker to be sent"""
    thumbnail: InputThumbnail | None = None
    """Sticker thumbnail; pass null to skip thumbnail uploading"""
    width: int
    """Sticker width"""
    height: int
    """Sticker height"""
    emoji: str
    """Emoji used to choose the sticker"""
