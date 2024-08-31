from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InviteLinkChatTypeSupergroup(BaseType):
    """
    The link is an invite link for a supergroup
    """

    __type__: Literal["inviteLinkChatTypeSupergroup"] = "inviteLinkChatTypeSupergroup"
