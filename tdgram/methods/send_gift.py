from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FormattedText, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SendGift(BaseMethod):
    """
    Sends a gift to another user. May return an error with a message 'STARGIFT_USAGE_LIMITED' if the gift was sold out
    """

    __type__: Literal["sendGift"] = "sendGift"
    __returning_type__ = Ok

    gift_id: int
    """Identifier of the gift to send"""
    user_id: int
    """Identifier of the user that will receive the gift"""
    text: FormattedText
    """Text to show along with the gift; 0-getOption('gift_text_length_max') characters. Only Bold, Italic, Underline, Strikethrough, Spoiler, and CustomEmoji entities are allowed"""
    is_private: bool
    """Pass true to show the current user as sender and gift text only to the gift receiver; otherwise, everyone will be able to see them"""
    pay_for_upgrade: bool
    """Pass true to additionally pay for the gift upgrade and allow the receiver to upgrade it for free"""
