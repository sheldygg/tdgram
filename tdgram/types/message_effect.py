from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageEffectType, Sticker


@dataclass(kw_only=True)
class MessageEffect(BaseType):
    """
    Contains information about an effect added to a message
    """

    __type__: Literal["messageEffect"] = "messageEffect"

    id: int
    """Unique identifier of the effect"""
    static_icon: Sticker | None = None
    """Static icon for the effect in WEBP format; may be null if none"""
    emoji: str
    """Emoji corresponding to the effect that can be used if static icon isn't available"""
    is_premium: bool
    """True, if Telegram Premium subscription is required to use the effect"""
    type: MessageEffectType
    """Type of the effect"""
