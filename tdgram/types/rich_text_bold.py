from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import RichText


@dataclass(kw_only=True)
class RichTextBold(BaseType):
    """
    A bold rich text
    """

    __type__: Literal["richTextBold"] = "richTextBold"

    text: RichText
    """Text"""
