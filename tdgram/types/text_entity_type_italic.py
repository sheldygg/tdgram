from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TextEntityTypeItalic(BaseType):
    """
    An italic text
    """

    __type__: Literal["textEntityTypeItalic"] = "textEntityTypeItalic"
