from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatMemberStatus


@dataclass(kw_only=True)
class ChatEventMemberSubscriptionExtended(BaseType):
    """
    A chat member extended their subscription to the chat
    """

    __type__: Literal["chatEventMemberSubscriptionExtended"] = (
        "chatEventMemberSubscriptionExtended"
    )

    user_id: int
    """Affected chat member user identifier"""
    old_status: ChatMemberStatus
    """Previous status of the chat member"""
    new_status: ChatMemberStatus
    """New status of the chat member"""
