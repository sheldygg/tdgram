from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatMemberStatus


@dataclass(kw_only=True)
class ChatEventMemberInvited(BaseType):
    """
    A new chat member was invited
    """

    __type__: Literal["chatEventMemberInvited"] = "chatEventMemberInvited"

    user_id: int
    """New member user identifier"""
    status: ChatMemberStatus
    """New member status"""
