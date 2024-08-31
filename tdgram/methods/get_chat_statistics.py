from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatStatistics
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatStatistics(BaseMethod):
    """
    Returns detailed statistics about a chat. Currently, this method can be used only for supergroups and channels. Can be used only if supergroupFullInfo.can_get_statistics == true
    """

    __type__: Literal["getChatStatistics"] = "getChatStatistics"
    __returning_type__ = ChatStatistics

    chat_id: int
    """Chat identifier"""
    is_dark: bool
    """Pass true if a dark theme is used by the application"""
