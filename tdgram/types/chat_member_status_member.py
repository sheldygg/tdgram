from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatMemberStatusMember(BaseType):
    """
    The user is a member of the chat, without any additional privileges or restrictions
    """

    __type__: Literal["chatMemberStatusMember"] = "chatMemberStatusMember"

    member_until_date: int
    """Point in time (Unix timestamp) when the user will be removed from the chat because of the expired subscription; 0 if never. Ignored in setChatMemberStatus"""
