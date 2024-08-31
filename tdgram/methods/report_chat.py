from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, ReportReason
from .base import BaseMethod


@dataclass(kw_only=True)
class ReportChat(BaseMethod):
    """
    Reports a chat to the Telegram moderators. A chat can be reported only from the chat action bar, or if chat.can_be_reported
    """

    __type__: Literal["reportChat"] = "reportChat"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    message_ids: list[int] | None = None
    """Identifiers of reported messages; may be empty to report the whole chat. Use messageProperties.can_be_reported to check whether the message can be reported"""
    reason: ReportReason
    """The reason for reporting the chat"""
    text: str
    """Additional report details; 0-1024 characters"""
