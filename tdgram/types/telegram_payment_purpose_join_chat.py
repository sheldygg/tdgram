from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TelegramPaymentPurposeJoinChat(BaseType):
    """
    The user joins a chat and subscribes to regular payments in Telegram Stars
    """

    __type__: Literal["telegramPaymentPurposeJoinChat"] = "telegramPaymentPurposeJoinChat"

    invite_link: str
    """Invite link to use"""
