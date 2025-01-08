from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import HttpUrl
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatRevenueWithdrawalUrl(BaseMethod):
    """
    Returns a URL for chat revenue withdrawal; requires owner privileges in the channel chat or the bot. Currently, this method can be used only
    """

    __type__: Literal["getChatRevenueWithdrawalUrl"] = "getChatRevenueWithdrawalUrl"
    __returning_type__ = HttpUrl

    chat_id: int
    """Chat identifier"""
    password: str
    """The 2-step verification password of the current user"""
