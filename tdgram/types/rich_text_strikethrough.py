from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import RichText


@dataclass(kw_only=True)
class RichTextStrikethrough(BaseType):
    """
    A strikethrough rich text
    """

    __type__: Literal["richTextStrikethrough"] = "richTextStrikethrough"

    text: RichText
    """Text"""
