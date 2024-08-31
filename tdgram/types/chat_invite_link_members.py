from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatInviteLinkMember


@dataclass(kw_only=True)
class ChatInviteLinkMembers(BaseType):
    """
    Contains a list of chat members joined a chat via an invite link
    """

    __type__: Literal["chatInviteLinkMembers"] = "chatInviteLinkMembers"

    total_count: int
    """Approximate total number of chat members found"""
    members: list[ChatInviteLinkMember]
    """List of chat members, joined a chat via an invite link"""
