from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import AnimatedEmoji


@dataclass(kw_only=True)
class MessageAnimatedEmoji(BaseType):
    """
    A message with an animated emoji
    """

    __type__: Literal["messageAnimatedEmoji"] = "messageAnimatedEmoji"

    animated_emoji: AnimatedEmoji
    """The animated emoji"""
    emoji: str
    """The corresponding emoji"""
