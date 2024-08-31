from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PageBlockCaption, Photo


@dataclass(kw_only=True)
class PageBlockEmbedded(BaseType):
    """
    An embedded web page
    """

    __type__: Literal["pageBlockEmbedded"] = "pageBlockEmbedded"

    url: str
    """URL of the embedded page, if available"""
    html: str
    """HTML-markup of the embedded page"""
    poster_photo: Photo | None = None
    """Poster photo, if available; may be null"""
    width: int
    """Block width; 0 if unknown"""
    height: int
    """Block height; 0 if unknown"""
    caption: PageBlockCaption
    """Block caption"""
    is_full_width: bool
    """True, if the block must be full width"""
    allow_scrolling: bool
    """True, if scrolling needs to be allowed"""
