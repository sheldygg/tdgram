from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeStickerSet(BaseType):
    """
    The link is a link to a sticker set. Call searchStickerSet with the given sticker set name to process the link and show the sticker set.
    """

    __type__: Literal["internalLinkTypeStickerSet"] = "internalLinkTypeStickerSet"

    sticker_set_name: str
    """Name of the sticker set"""
    expect_custom_emoji: bool
    """True, if the sticker set is expected to contain custom emoji"""
