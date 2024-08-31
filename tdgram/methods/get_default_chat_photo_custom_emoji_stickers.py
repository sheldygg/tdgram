from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Stickers
from .base import BaseMethod


@dataclass(kw_only=True)
class GetDefaultChatPhotoCustomEmojiStickers(BaseMethod):
    """
    Returns default list of custom emoji stickers for placing on a chat photo
    """

    __type__: Literal["getDefaultChatPhotoCustomEmojiStickers"] = (
        "getDefaultChatPhotoCustomEmojiStickers"
    )
    __returning_type__ = Stickers
