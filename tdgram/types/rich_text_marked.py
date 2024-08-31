from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import RichText


@dataclass(kw_only=True)
class RichTextMarked(BaseType):
    """
    A marked rich text
    """

    __type__: Literal["richTextMarked"] = "richTextMarked"

    text: RichText
    """Text"""
