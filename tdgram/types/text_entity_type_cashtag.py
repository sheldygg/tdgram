from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TextEntityTypeCashtag(BaseType):
    """
    A cashtag text, beginning with '$' and consisting of capital English letters (e.g., '$USD')
    """

    __type__: Literal["textEntityTypeCashtag"] = "textEntityTypeCashtag"
