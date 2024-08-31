from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageStatistics
from .base import BaseMethod


@dataclass(kw_only=True)
class GetMessageStatistics(BaseMethod):
    """
    Returns detailed statistics about a message. Can be used only if messageProperties.can_get_statistics == true
    """

    __type__: Literal["getMessageStatistics"] = "getMessageStatistics"
    __returning_type__ = MessageStatistics

    chat_id: int
    """Chat identifier"""
    message_id: int
    """Message identifier"""
    is_dark: bool
    """Pass true if a dark theme is used by the application"""
