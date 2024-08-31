from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Stickers
from .base import BaseMethod


@dataclass(kw_only=True)
class GetCustomEmojiReactionAnimations(BaseMethod):
    """
    Returns TGS stickers with generic animations for custom emoji reactions
    """

    __type__: Literal["getCustomEmojiReactionAnimations"] = "getCustomEmojiReactionAnimations"
    __returning_type__ = Stickers
