from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Sticker


@dataclass(kw_only=True)
class MessageGiveawayPrizeStars(BaseType):
    """
    A Telegram Stars were received by the current user from a giveaway
    """

    __type__: Literal["messageGiveawayPrizeStars"] = "messageGiveawayPrizeStars"

    star_count: int
    """Number of Telegram Stars that were received"""
    transaction_id: str
    """Identifier of the transaction for Telegram Stars credit"""
    boosted_chat_id: int
    """Identifier of the supergroup or channel chat, which was automatically boosted by the winners of the giveaway"""
    giveaway_message_id: int
    """Identifier of the message with the giveaway in the boosted chat; can be 0 if the message was deleted"""
    is_unclaimed: bool
    """True, if the corresponding winner wasn't chosen and the Telegram Stars were received by the owner of the boosted chat"""
    sticker: Sticker | None = None
    """A sticker to be shown in the message; may be null if unknown"""
