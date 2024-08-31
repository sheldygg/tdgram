from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatPermissions


@dataclass(kw_only=True)
class ChatMemberStatusRestricted(BaseType):
    """
    The user is under certain restrictions in the chat. Not supported in basic groups and channels
    """

    __type__: Literal["chatMemberStatusRestricted"] = "chatMemberStatusRestricted"

    is_member: bool
    """True, if the user is a member of the chat"""
    restricted_until_date: int
    """Point in time (Unix timestamp) when restrictions will be lifted from the user; 0 if never. If the user is restricted for more than 366 days or for less than 30 seconds from the current time, the user is considered to be restricted forever"""
    permissions: ChatPermissions
    """User permissions in the chat"""
