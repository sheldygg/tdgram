from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Photo


@dataclass(kw_only=True)
class PageBlockRelatedArticle(BaseType):
    """
    Contains information about a related article
    """

    __type__: Literal["pageBlockRelatedArticle"] = "pageBlockRelatedArticle"

    url: str
    """Related article URL"""
    title: str | None = None
    """Article title; may be empty"""
    description: str | None = None
    """Article description; may be empty"""
    photo: Photo | None = None
    """Article photo; may be null"""
    author: str | None = None
    """Article author; may be empty"""
    publish_date: int
    """Point in time (Unix timestamp) when the article was published; 0 if unknown"""
