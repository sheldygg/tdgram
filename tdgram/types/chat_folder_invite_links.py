from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatFolderInviteLink


@dataclass(kw_only=True)
class ChatFolderInviteLinks(BaseType):
    """
    Represents a list of chat folder invite links
    """

    __type__: Literal["chatFolderInviteLinks"] = "chatFolderInviteLinks"

    invite_links: list[ChatFolderInviteLink]
    """List of the invite links"""
