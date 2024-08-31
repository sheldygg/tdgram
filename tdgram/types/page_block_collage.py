from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PageBlock, PageBlockCaption


@dataclass(kw_only=True)
class PageBlockCollage(BaseType):
    """
    A collage
    """

    __type__: Literal["pageBlockCollage"] = "pageBlockCollage"

    page_blocks: list[PageBlock]
    """Collage item contents"""
    caption: PageBlockCaption
    """Block caption"""
