from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TextEntityTypeExpandableBlockQuote(BaseType):
    """
    Text that must be formatted as if inside a blockquote HTML tag and collapsed by default to 3 lines with the ability to show full text; not supported in secret chats
    """

    __type__: Literal["textEntityTypeExpandableBlockQuote"] = "textEntityTypeExpandableBlockQuote"
