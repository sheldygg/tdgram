from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Animation, FormattedText


@dataclass(kw_only=True)
class MessageAnimation(BaseType):
    """
    An animation message (GIF-style).
    """

    __type__: Literal["messageAnimation"] = "messageAnimation"

    animation: Animation
    """The animation description"""
    caption: FormattedText
    """Animation caption"""
    show_caption_above_media: bool
    """True, if the caption must be shown above the animation; otherwise, the caption must be shown below the animation"""
    has_spoiler: bool
    """True, if the animation preview must be covered by a spoiler animation"""
    is_secret: bool
    """True, if the animation thumbnail must be blurred and the animation must be shown only while tapped"""
