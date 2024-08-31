from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import RichText


@dataclass(kw_only=True)
class PageBlockPullQuote(BaseType):
    """
    A pull quote
    """

    __type__: Literal["pageBlockPullQuote"] = "pageBlockPullQuote"

    text: RichText
    """Quote text"""
    credit: RichText
    """Quote credit"""
