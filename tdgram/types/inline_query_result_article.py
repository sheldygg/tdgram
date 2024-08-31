from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Thumbnail


@dataclass(kw_only=True)
class InlineQueryResultArticle(BaseType):
    """
    Represents a link to an article or web page
    """

    __type__: Literal["inlineQueryResultArticle"] = "inlineQueryResultArticle"

    id: str
    """Unique identifier of the query result"""
    url: str
    """URL of the result, if it exists"""
    hide_url: bool
    """True, if the URL must be not shown"""
    title: str
    """Title of the result"""
    description: str
    """A short description of the result"""
    thumbnail: Thumbnail | None = None
    """Result thumbnail in JPEG format; may be null"""
