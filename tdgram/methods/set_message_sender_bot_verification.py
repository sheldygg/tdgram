from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageSender, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetMessageSenderBotVerification(BaseMethod):
    """
    Changes the verification status of a user or a chat by an owned bot
    """

    __type__: Literal["setMessageSenderBotVerification"] = "setMessageSenderBotVerification"
    __returning_type__ = Ok

    bot_user_id: int
    """Identifier of the owned bot, which will verify the user or the chat"""
    verified_id: MessageSender
    """Identifier of the user or the supergroup or channel chat, which will be verified by the bot"""
    custom_description: str
    """Custom description of verification reason; 0-getOption('bot_verification_custom_description_length_max')."""
