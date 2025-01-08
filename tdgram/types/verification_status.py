from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class VerificationStatus(BaseType):
    """
    Contains information about verification status of a chat or a user
    """

    __type__: Literal["verificationStatus"] = "verificationStatus"

    is_verified: bool
    """True, if the chat or the user is verified by Telegram"""
    is_scam: bool
    """True, if the chat or the user is marked as scam by Telegram"""
    is_fake: bool
    """True, if the chat or the user is marked as fake by Telegram"""
    bot_verification_icon_custom_emoji_id: int
    """Identifier of the custom emoji to be shown as verification sign provided by a bot for the user; 0 if none"""
