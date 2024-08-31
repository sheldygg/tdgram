from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatEventInvitesToggled(BaseType):
    """
    The can_invite_users permission of a supergroup chat was toggled
    """

    __type__: Literal["chatEventInvitesToggled"] = "chatEventInvitesToggled"

    can_invite_users: bool
    """New value of can_invite_users permission"""
