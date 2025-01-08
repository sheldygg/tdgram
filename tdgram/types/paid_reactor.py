from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageSender


@dataclass(kw_only=True)
class PaidReactor(BaseType):
    """
    Contains information about a user that added paid reactions
    """

    __type__: Literal["paidReactor"] = "paidReactor"

    sender_id: MessageSender | None = None
    """Identifier of the user or chat that added the reactions; may be null for anonymous reactors that aren't the current user"""
    star_count: int
    """Number of Telegram Stars added"""
    is_top: bool
    """True, if the reactor is one of the most active reactors; may be false if the reactor is the current user"""
    is_me: bool
    """True, if the paid reaction was added by the current user"""
    is_anonymous: bool
    """True, if the reactor is anonymous"""
