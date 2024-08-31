from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatAdministratorRights


@dataclass(kw_only=True)
class ChatMemberStatusAdministrator(BaseType):
    """
    The user is a member of the chat and has some additional privileges. In basic groups, administrators can edit and delete messages sent by others, add new members, ban unprivileged members, and manage video chats.
    """

    __type__: Literal["chatMemberStatusAdministrator"] = "chatMemberStatusAdministrator"

    custom_title: str
    """A custom title of the administrator; 0-16 characters without emoji; applicable to supergroups only"""
    can_be_edited: bool
    """True, if the current user can edit the administrator privileges for the called user"""
    rights: ChatAdministratorRights
    """Rights of the administrator"""
