from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatPhotoSticker


@dataclass(kw_only=True)
class InputChatPhotoSticker(BaseType):
    """
    A sticker on a custom background
    """

    __type__: Literal["inputChatPhotoSticker"] = "inputChatPhotoSticker"

    sticker: ChatPhotoSticker
    """Information about the sticker"""
