from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PageBlock, PageBlockCaption


@dataclass(kw_only=True)
class PageBlockSlideshow(BaseType):
    """
    A slideshow
    """

    __type__: Literal["pageBlockSlideshow"] = "pageBlockSlideshow"

    page_blocks: list[PageBlock]
    """Slideshow item contents"""
    caption: PageBlockCaption
    """Block caption"""
