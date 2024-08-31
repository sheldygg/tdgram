from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TextEntityTypeTextUrl(BaseType):
    """
    A text description shown instead of a raw URL
    """

    __type__: Literal["textEntityTypeTextUrl"] = "textEntityTypeTextUrl"

    url: str
    """HTTP or tg:// URL to be opened when the link is clicked"""
