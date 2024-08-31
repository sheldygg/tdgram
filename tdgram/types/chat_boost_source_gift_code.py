from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatBoostSourceGiftCode(BaseType):
    """
    The chat created a Telegram Premium gift code for a user
    """

    __type__: Literal["chatBoostSourceGiftCode"] = "chatBoostSourceGiftCode"

    user_id: int
    """Identifier of a user, for which the gift code was created"""
    gift_code: str
    """The created Telegram Premium gift code, which is known only if this is a gift code for the current user, or it has already been claimed"""
