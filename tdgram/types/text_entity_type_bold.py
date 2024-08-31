from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TextEntityTypeBold(BaseType):
    """
    A bold text
    """

    __type__: Literal["textEntityTypeBold"] = "textEntityTypeBold"
