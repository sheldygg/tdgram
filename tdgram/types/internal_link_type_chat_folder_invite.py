from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeChatFolderInvite(BaseType):
    """
    The link is an invite link to a chat folder. Call checkChatFolderInviteLink with the given invite link to process the link.
    """

    __type__: Literal["internalLinkTypeChatFolderInvite"] = "internalLinkTypeChatFolderInvite"

    invite_link: str
    """Internal representation of the invite link"""
