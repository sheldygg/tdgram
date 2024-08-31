from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PageBlock, PageBlockCaption, Photo


@dataclass(kw_only=True)
class PageBlockEmbeddedPost(BaseType):
    """
    An embedded post
    """

    __type__: Literal["pageBlockEmbeddedPost"] = "pageBlockEmbeddedPost"

    url: str
    """URL of the embedded post"""
    author: str
    """Post author"""
    author_photo: Photo | None = None
    """Post author photo; may be null"""
    date: int
    """Point in time (Unix timestamp) when the post was created; 0 if unknown"""
    page_blocks: list[PageBlock]
    """Post content"""
    caption: PageBlockCaption
    """Post caption"""
