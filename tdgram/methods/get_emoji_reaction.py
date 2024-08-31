from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import EmojiReaction
from .base import BaseMethod


@dataclass(kw_only=True)
class GetEmojiReaction(BaseMethod):
    """
    Returns information about an emoji reaction. Returns a 404 error if the reaction is not found
    """

    __type__: Literal["getEmojiReaction"] = "getEmojiReaction"
    __returning_type__ = EmojiReaction

    emoji: str
    """Text representation of the reaction"""
