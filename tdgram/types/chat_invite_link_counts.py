from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatInviteLinkCount


@dataclass(kw_only=True)
class ChatInviteLinkCounts(BaseType):
    """
    Contains a list of chat invite link counts
    """

    __type__: Literal["chatInviteLinkCounts"] = "chatInviteLinkCounts"

    invite_link_counts: list[ChatInviteLinkCount]
    """List of invite link counts"""
