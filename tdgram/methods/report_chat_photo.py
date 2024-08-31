from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, ReportReason
from .base import BaseMethod


@dataclass(kw_only=True)
class ReportChatPhoto(BaseMethod):
    """
    Reports a chat photo to the Telegram moderators. A chat photo can be reported only if chat.can_be_reported
    """

    __type__: Literal["reportChatPhoto"] = "reportChatPhoto"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    file_id: int
    """Identifier of the photo to report. Only full photos from chatPhoto can be reported"""
    reason: ReportReason
    """The reason for reporting the chat photo"""
    text: str
    """Additional report details; 0-1024 characters"""
