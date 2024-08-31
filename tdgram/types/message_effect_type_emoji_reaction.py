from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Sticker


@dataclass(kw_only=True)
class MessageEffectTypeEmojiReaction(BaseType):
    """
    An effect from an emoji reaction
    """

    __type__: Literal["messageEffectTypeEmojiReaction"] = "messageEffectTypeEmojiReaction"

    select_animation: Sticker
    """Select animation for the effect in TGS format"""
    effect_animation: Sticker
    """Effect animation for the effect in TGS format"""
