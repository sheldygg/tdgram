from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import HttpUrl, MessageSender
from .base import BaseMethod


@dataclass(kw_only=True)
class GetStarWithdrawalUrl(BaseMethod):
    """
    Returns a URL for Telegram Star withdrawal
    """

    __type__: Literal["getStarWithdrawalUrl"] = "getStarWithdrawalUrl"
    __returning_type__ = HttpUrl

    owner_id: MessageSender
    """Identifier of the owner of the Telegram Stars; can be identifier of an owned bot, or identifier of an owned channel chat"""
    star_count: int
    """The number of Telegram Stars to withdraw. Must be at least getOption('star_withdrawal_count_min')"""
    password: str
    """The 2-step verification password of the current user"""
