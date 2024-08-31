from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class RichTextPlain(BaseType):
    """
    A plain text
    """

    __type__: Literal["richTextPlain"] = "richTextPlain"

    text: str
    """Text"""
