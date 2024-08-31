from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Sticker


@dataclass(kw_only=True)
class DiceStickersSlotMachine(BaseType):
    """
    Animated stickers to be combined into a slot machine
    """

    __type__: Literal["diceStickersSlotMachine"] = "diceStickersSlotMachine"

    background: Sticker
    """The animated sticker with the slot machine background. The background animation must start playing after all reel animations finish"""
    lever: Sticker
    """The animated sticker with the lever animation. The lever animation must play once in the initial dice state"""
    left_reel: Sticker
    """The animated sticker with the left reel"""
    center_reel: Sticker
    """The animated sticker with the center reel"""
    right_reel: Sticker
    """The animated sticker with the right reel"""
