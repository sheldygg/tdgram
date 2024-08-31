from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TextEntityTypeMentionName(BaseType):
    """
    A text shows instead of a raw mention of the user (e.g., when the user has no username)
    """

    __type__: Literal["textEntityTypeMentionName"] = "textEntityTypeMentionName"

    user_id: int
    """Identifier of the mentioned user"""
