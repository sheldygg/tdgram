from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StickerFormatTgs(BaseType):
    """
    The sticker is an animation in TGS format
    """

    __type__: Literal["stickerFormatTgs"] = "stickerFormatTgs"
