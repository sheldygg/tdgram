from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PaidMedia


@dataclass(kw_only=True)
class ChannelTransactionPurposePaidMedia(BaseType):
    """
    Paid media were bought
    """

    __type__: Literal["channelTransactionPurposePaidMedia"] = "channelTransactionPurposePaidMedia"

    message_id: int
    """Identifier of the corresponding message with paid media; can be an identifier of a deleted message"""
    media: list[PaidMedia]
    """The bought media if the trancastion wasn't refunded"""
