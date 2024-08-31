from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import RichText


@dataclass(kw_only=True)
class PageBlockParagraph(BaseType):
    """
    A text paragraph
    """

    __type__: Literal["pageBlockParagraph"] = "pageBlockParagraph"

    text: RichText
    """Paragraph text"""
