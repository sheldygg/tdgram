from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class Text(BaseType):
    """
    Contains some text
    """

    __type__: Literal["text"] = "text"

    text: str
    """Text"""
