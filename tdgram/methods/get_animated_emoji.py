from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import AnimatedEmoji
from .base import BaseMethod


@dataclass(kw_only=True)
class GetAnimatedEmoji(BaseMethod):
    """
    Returns an animated emoji corresponding to a given emoji. Returns a 404 error if the emoji has no animated emoji
    """

    __type__: Literal["getAnimatedEmoji"] = "getAnimatedEmoji"
    __returning_type__ = AnimatedEmoji

    emoji: str
    """The emoji"""
