from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Animation


@dataclass(kw_only=True)
class LinkPreviewTypeAnimation(BaseType):
    """
    The link is a link to an animation
    """

    __type__: Literal["linkPreviewTypeAnimation"] = "linkPreviewTypeAnimation"

    animation: Animation
    """The animation"""
    author: str
    """Author of the animation"""
