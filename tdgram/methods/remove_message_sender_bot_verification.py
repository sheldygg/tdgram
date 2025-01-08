from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageSender, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RemoveMessageSenderBotVerification(BaseMethod):
    """
    Removes the verification status of a user or a chat by an owned bot
    """

    __type__: Literal["removeMessageSenderBotVerification"] = "removeMessageSenderBotVerification"
    __returning_type__ = Ok

    bot_user_id: int
    """Identifier of the owned bot, which verified the user or the chat"""
    verified_id: MessageSender
    """Identifier of the user or the supergroup or channel chat, which verification is removed"""
