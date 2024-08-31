from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import File


@dataclass(kw_only=True)
class StickerFullTypeRegular(BaseType):
    """
    The sticker is a regular sticker
    """

    __type__: Literal["stickerFullTypeRegular"] = "stickerFullTypeRegular"

    premium_animation: File | None = None
    """Premium animation of the sticker; may be null. If present, only Telegram Premium users can use the sticker"""
