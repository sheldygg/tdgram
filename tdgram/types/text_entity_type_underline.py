from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TextEntityTypeUnderline(BaseType):
    """
    An underlined text
    """

    __type__: Literal["textEntityTypeUnderline"] = "textEntityTypeUnderline"
