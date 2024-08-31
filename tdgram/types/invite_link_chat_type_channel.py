from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InviteLinkChatTypeChannel(BaseType):
    """
    The link is an invite link for a channel
    """

    __type__: Literal["inviteLinkChatTypeChannel"] = "inviteLinkChatTypeChannel"
