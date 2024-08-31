from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatAction, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SendChatAction(BaseMethod):
    """
    Sends a notification about user activity in a chat
    """

    __type__: Literal["sendChatAction"] = "sendChatAction"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    message_thread_id: int
    """If not 0, the message thread identifier in which the action was performed"""
    business_connection_id: str
    """Unique identifier of business connection on behalf of which to send the request; for bots only"""
    action: ChatAction | None = None
    """The action description; pass null to cancel the currently active action"""
