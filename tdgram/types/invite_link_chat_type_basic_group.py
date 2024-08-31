from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InviteLinkChatTypeBasicGroup(BaseType):
    """
    The link is an invite link for a basic group
    """

    __type__: Literal["inviteLinkChatTypeBasicGroup"] = "inviteLinkChatTypeBasicGroup"
