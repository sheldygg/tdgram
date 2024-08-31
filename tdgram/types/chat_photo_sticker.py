from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BackgroundFill, ChatPhotoStickerType


@dataclass(kw_only=True)
class ChatPhotoSticker(BaseType):
    """
    Information about the sticker, which was used to create the chat photo. The sticker is shown at the center of the photo and occupies at most 67% of it
    """

    __type__: Literal["chatPhotoSticker"] = "chatPhotoSticker"

    type: ChatPhotoStickerType
    """Type of the sticker"""
    background_fill: BackgroundFill
    """The fill to be used as background for the sticker; rotation angle in backgroundFillGradient isn't supported"""
