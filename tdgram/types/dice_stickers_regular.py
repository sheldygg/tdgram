from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Sticker


@dataclass(kw_only=True)
class DiceStickersRegular(BaseType):
    """
    A regular animated sticker
    """

    __type__: Literal["diceStickersRegular"] = "diceStickersRegular"

    sticker: Sticker
    """The animated sticker with the dice animation"""
