from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChannelTransactionPurposeJoin(BaseType):
    """
    User joined the channel and subscribed to regular payments in Telegram Stars
    """

    __type__: Literal["channelTransactionPurposeJoin"] = "channelTransactionPurposeJoin"

    period: int
    """The number of seconds between consecutive Telegram Star debiting"""
