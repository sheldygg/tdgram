from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PageBlockRelatedArticle, RichText


@dataclass(kw_only=True)
class PageBlockRelatedArticles(BaseType):
    """
    Related articles
    """

    __type__: Literal["pageBlockRelatedArticles"] = "pageBlockRelatedArticles"

    header: RichText
    """Block header"""
    articles: list[PageBlockRelatedArticle]
    """List of related articles"""
