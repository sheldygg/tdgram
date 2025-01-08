from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Photo


@dataclass(kw_only=True)
class LinkPreviewTypeEmbeddedAnimationPlayer(BaseType):
    """
    The link is a link to an animation player
    """

    __type__: Literal["linkPreviewTypeEmbeddedAnimationPlayer"] = (
        "linkPreviewTypeEmbeddedAnimationPlayer"
    )

    url: str
    """URL of the external animation player"""
    thumbnail: Photo | None = None
    """Thumbnail of the animation; may be null if unknown"""
    duration: int
    """Duration of the animation, in seconds"""
    width: int
    """Expected width of the embedded player"""
    height: int
    """Expected height of the embedded player"""
