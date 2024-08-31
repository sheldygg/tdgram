from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatBoostSourcePremium(BaseType):
    """
    A user with Telegram Premium subscription or gifted Telegram Premium boosted the chat
    """

    __type__: Literal["chatBoostSourcePremium"] = "chatBoostSourcePremium"

    user_id: int
    """Identifier of the user"""
