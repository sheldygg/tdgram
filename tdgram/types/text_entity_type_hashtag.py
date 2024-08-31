from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TextEntityTypeHashtag(BaseType):
    """
    A hashtag text, beginning with '#'
    """

    __type__: Literal["textEntityTypeHashtag"] = "textEntityTypeHashtag"
