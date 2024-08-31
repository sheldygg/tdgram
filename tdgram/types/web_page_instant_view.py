from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InternalLinkType, PageBlock


@dataclass(kw_only=True)
class WebPageInstantView(BaseType):
    """
    Describes an instant view page for a web page
    """

    __type__: Literal["webPageInstantView"] = "webPageInstantView"

    page_blocks: list[PageBlock]
    """Content of the instant view page"""
    view_count: int
    """Number of the instant view views; 0 if unknown"""
    version: int
    """Version of the instant view; currently, can be 1 or 2"""
    is_rtl: bool
    """True, if the instant view must be shown from right to left"""
    is_full: bool
    """True, if the instant view contains the full page. A network request might be needed to get the full instant view"""
    feedback_link: InternalLinkType
    """An internal link to be opened to leave feedback about the instant view"""
