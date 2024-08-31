from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatMemberStatus


@dataclass(kw_only=True)
class ChatEventMemberPromoted(BaseType):
    """
    A chat member has gained/lost administrator status, or the list of their administrator privileges has changed
    """

    __type__: Literal["chatEventMemberPromoted"] = "chatEventMemberPromoted"

    user_id: int
    """Affected chat member user identifier"""
    old_status: ChatMemberStatus
    """Previous status of the chat member"""
    new_status: ChatMemberStatus
    """New status of the chat member"""
