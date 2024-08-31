from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatInviteLink


@dataclass(kw_only=True)
class ChatEventInviteLinkEdited(BaseType):
    """
    A chat invite link was edited
    """

    __type__: Literal["chatEventInviteLinkEdited"] = "chatEventInviteLinkEdited"

    old_invite_link: ChatInviteLink
    """Previous information about the invite link"""
    new_invite_link: ChatInviteLink
    """New information about the invite link"""
