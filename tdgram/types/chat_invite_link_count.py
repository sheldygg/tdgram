from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatInviteLinkCount(BaseType):
    """
    Describes a chat administrator with a number of active and revoked chat invite links
    """

    __type__: Literal["chatInviteLinkCount"] = "chatInviteLinkCount"

    user_id: int
    """Administrator's user identifier"""
    invite_link_count: int
    """Number of active invite links"""
    revoked_invite_link_count: int
    """Number of revoked invite links"""
