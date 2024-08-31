from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Sticker


@dataclass(kw_only=True)
class Stickers(BaseType):
    """
    Represents a list of stickers
    """

    __type__: Literal["stickers"] = "stickers"

    stickers: list[Sticker]
    """List of stickers"""
