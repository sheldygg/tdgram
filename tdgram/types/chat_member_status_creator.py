from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatMemberStatusCreator(BaseType):
    """
    The user is the owner of the chat and has all the administrator privileges
    """

    __type__: Literal["chatMemberStatusCreator"] = "chatMemberStatusCreator"

    custom_title: str
    """A custom title of the owner; 0-16 characters without emoji; applicable to supergroups only"""
    is_anonymous: bool
    """True, if the creator isn't shown in the chat member list and sends messages anonymously; applicable to supergroups only"""
    is_member: bool
    """True, if the user is a member of the chat"""
