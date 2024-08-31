from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import RichText


@dataclass(kw_only=True)
class PageBlockAuthorDate(BaseType):
    """
    The author and publishing date of a page
    """

    __type__: Literal["pageBlockAuthorDate"] = "pageBlockAuthorDate"

    author: RichText
    """Author"""
    publish_date: int
    """Point in time (Unix timestamp) when the article was published; 0 if unknown"""
