from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TextEntityTypeMention(BaseType):
    """
    A mention of a user, a supergroup, or a channel by their username
    """

    __type__: Literal["textEntityTypeMention"] = "textEntityTypeMention"
