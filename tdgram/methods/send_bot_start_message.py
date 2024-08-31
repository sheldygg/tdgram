from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Message
from .base import BaseMethod


@dataclass(kw_only=True)
class SendBotStartMessage(BaseMethod):
    """
    Invites a bot to a chat (if it is not yet a member) and sends it the /start command; requires can_invite_users member right. Bots can't be invited to a private chat other than the chat with the bot.
    """

    __type__: Literal["sendBotStartMessage"] = "sendBotStartMessage"
    __returning_type__ = Message

    bot_user_id: int
    """Identifier of the bot"""
    chat_id: int
    """Identifier of the target chat"""
    parameter: str
    """A hidden parameter sent to the bot for deep linking purposes (https://core.telegram.org/bots#deep-linking)"""
