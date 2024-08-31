from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChannelTransactionPurposeReaction(BaseType):
    """
    User paid for a reaction
    """

    __type__: Literal["channelTransactionPurposeReaction"] = "channelTransactionPurposeReaction"

    message_id: int
    """Identifier of the reacted message; can be an identifier of a deleted message"""
