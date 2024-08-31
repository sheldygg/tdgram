from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InlineKeyboardButtonTypeUser(BaseType):
    """
    A button with a user reference to be handled in the same way as textEntityTypeMentionName entities
    """

    __type__: Literal["inlineKeyboardButtonTypeUser"] = "inlineKeyboardButtonTypeUser"

    user_id: int
    """User identifier"""
