from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatInviteLink


@dataclass(kw_only=True)
class ChatEventInviteLinkDeleted(BaseType):
    """
    A revoked chat invite link was deleted
    """

    __type__: Literal["chatEventInviteLinkDeleted"] = "chatEventInviteLinkDeleted"

    invite_link: ChatInviteLink
    """The invite link"""
