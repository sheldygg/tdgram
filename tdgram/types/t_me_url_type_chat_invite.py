from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatInviteLinkInfo


@dataclass(kw_only=True)
class TMeUrlTypeChatInvite(BaseType):
    """
    A chat invite link
    """

    __type__: Literal["tMeUrlTypeChatInvite"] = "tMeUrlTypeChatInvite"

    info: ChatInviteLinkInfo
    """Information about the chat invite link"""
