from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatPhoto, InviteLinkChatType


@dataclass(kw_only=True)
class LinkPreviewTypeChat(BaseType):
    """
    The link is a link to a chat
    """

    __type__: Literal["linkPreviewTypeChat"] = "linkPreviewTypeChat"

    type: InviteLinkChatType
    """Type of the chat"""
    photo: ChatPhoto | None = None
    """Photo of the chat; may be null"""
    creates_join_request: bool
    """True, if the link only creates join request"""
