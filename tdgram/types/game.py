from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Animation, FormattedText, Photo


@dataclass(kw_only=True)
class Game(BaseType):
    """
    Describes a game. Use getInternalLink with internalLinkTypeGame to share the game
    """

    __type__: Literal["game"] = "game"

    id: int
    """Unique game identifier"""
    short_name: str
    """Game short name"""
    title: str
    """Game title"""
    text: FormattedText
    """Game text, usually containing scoreboards for a game"""
    description: str
    """Game description"""
    photo: Photo
    """Game photo"""
    animation: Animation | None = None
    """Game animation; may be null"""
