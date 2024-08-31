from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageSender, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ReportMessageReactions(BaseMethod):
    """
    Reports reactions set on a message to the Telegram moderators. Reactions on a message can be reported only if messageProperties.can_report_reactions
    """

    __type__: Literal["reportMessageReactions"] = "reportMessageReactions"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    message_id: int
    """Message identifier"""
    sender_id: MessageSender
    """Identifier of the sender, which added the reaction"""
