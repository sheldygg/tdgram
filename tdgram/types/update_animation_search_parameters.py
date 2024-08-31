from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateAnimationSearchParameters(BaseType):
    """
    The parameters of animation search through getOption('animation_search_bot_username') bot has changed
    """

    __type__: Literal["updateAnimationSearchParameters"] = "updateAnimationSearchParameters"

    provider: str
    """Name of the animation search provider"""
    emojis: list[str]
    """The new list of emojis suggested for searching"""
