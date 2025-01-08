from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ReportChatResult
from .base import BaseMethod


@dataclass(kw_only=True)
class ReportChat(BaseMethod):
    """
    Reports a chat to the Telegram moderators. A chat can be reported only from the chat action bar, or if chat.can_be_reported
    """

    __type__: Literal["reportChat"] = "reportChat"
    __returning_type__ = ReportChatResult

    chat_id: int
    """Chat identifier"""
    option_id: bytes
    """Option identifier chosen by the user; leave empty for the initial request"""
    message_ids: list[int]
    """Identifiers of reported messages. Use messageProperties.can_report_chat to check whether the message can be reported"""
    text: str
    """Additional report details if asked by the server; 0-1024 characters; leave empty for the initial request"""
