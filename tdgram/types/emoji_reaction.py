from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Sticker


@dataclass(kw_only=True)
class EmojiReaction(BaseType):
    """
    Contains information about an emoji reaction
    """

    __type__: Literal["emojiReaction"] = "emojiReaction"

    emoji: str
    """Text representation of the reaction"""
    title: str
    """Reaction title"""
    is_active: bool
    """True, if the reaction can be added to new messages and enabled in chats"""
    static_icon: Sticker
    """Static icon for the reaction"""
    appear_animation: Sticker
    """Appear animation for the reaction"""
    select_animation: Sticker
    """Select animation for the reaction"""
    activate_animation: Sticker
    """Activate animation for the reaction"""
    effect_animation: Sticker
    """Effect animation for the reaction"""
    around_animation: Sticker | None = None
    """Around animation for the reaction; may be null"""
    center_animation: Sticker | None = None
    """Center animation for the reaction; may be null"""
