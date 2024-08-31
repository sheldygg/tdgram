from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Animation, PageBlockCaption


@dataclass(kw_only=True)
class PageBlockAnimation(BaseType):
    """
    An animation
    """

    __type__: Literal["pageBlockAnimation"] = "pageBlockAnimation"

    animation: Animation | None = None
    """Animation file; may be null"""
    caption: PageBlockCaption
    """Animation caption"""
    need_autoplay: bool
    """True, if the animation must be played automatically"""
