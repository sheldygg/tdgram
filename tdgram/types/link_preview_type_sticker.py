from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Sticker


@dataclass(kw_only=True)
class LinkPreviewTypeSticker(BaseType):
    """
    The link is a link to a sticker
    """

    __type__: Literal["linkPreviewTypeSticker"] = "linkPreviewTypeSticker"

    sticker: Sticker
    """The sticker. It can be an arbitrary WEBP image and can have dimensions bigger than 512"""
