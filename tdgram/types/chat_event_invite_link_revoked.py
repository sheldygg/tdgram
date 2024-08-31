from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatInviteLink


@dataclass(kw_only=True)
class ChatEventInviteLinkRevoked(BaseType):
    """
    A chat invite link was revoked
    """

    __type__: Literal["chatEventInviteLinkRevoked"] = "chatEventInviteLinkRevoked"

    invite_link: ChatInviteLink
    """The invite link"""
