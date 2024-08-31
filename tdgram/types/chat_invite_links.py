from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatInviteLink


@dataclass(kw_only=True)
class ChatInviteLinks(BaseType):
    """
    Contains a list of chat invite links
    """

    __type__: Literal["chatInviteLinks"] = "chatInviteLinks"

    total_count: int
    """Approximate total number of chat invite links found"""
    invite_links: list[ChatInviteLink]
    """List of invite links"""
