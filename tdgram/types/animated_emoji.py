from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import File, Sticker


@dataclass(kw_only=True)
class AnimatedEmoji(BaseType):
    """
    Describes an animated or custom representation of an emoji
    """

    __type__: Literal["animatedEmoji"] = "animatedEmoji"

    sticker: Sticker | None = None
    """Sticker for the emoji; may be null if yet unknown for a custom emoji. If the sticker is a custom emoji, then it can have arbitrary format"""
    sticker_width: int
    """Expected width of the sticker, which can be used if the sticker is null"""
    sticker_height: int
    """Expected height of the sticker, which can be used if the sticker is null"""
    fitzpatrick_type: int
    """Emoji modifier fitzpatrick type; 0-6; 0 if none"""
    sound: File | None = None
    """File containing the sound to be played when the sticker is clicked; may be null. The sound is encoded with the Opus codec, and stored inside an OGG container"""
