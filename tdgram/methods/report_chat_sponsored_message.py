from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ReportChatSponsoredMessageResult
from .base import BaseMethod


@dataclass(kw_only=True)
class ReportChatSponsoredMessage(BaseMethod):
    """
    Reports a sponsored message to Telegram moderators
    """

    __type__: Literal["reportChatSponsoredMessage"] = "reportChatSponsoredMessage"
    __returning_type__ = ReportChatSponsoredMessageResult

    chat_id: int
    """Chat identifier of the sponsored message"""
    message_id: int
    """Identifier of the sponsored message"""
    option_id: bytes
    """Option identifier chosen by the user; leave empty for the initial request"""
