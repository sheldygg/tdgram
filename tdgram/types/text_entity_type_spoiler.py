from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TextEntityTypeSpoiler(BaseType):
    """
    A spoiler text
    """

    __type__: Literal["textEntityTypeSpoiler"] = "textEntityTypeSpoiler"
