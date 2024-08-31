from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TextEntityTypePreCode(BaseType):
    """
    Text that must be formatted as if inside pre, and code HTML tags
    """

    __type__: Literal["textEntityTypePreCode"] = "textEntityTypePreCode"

    language: str
    """Programming language of the code; as defined by the sender"""
