from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeChatInvite(BaseType):
    """
    The link is a chat invite link. Call checkChatInviteLink with the given invite link to process the link.
    """

    __type__: Literal["internalLinkTypeChatInvite"] = "internalLinkTypeChatInvite"

    invite_link: str
    """Internal representation of the invite link"""
