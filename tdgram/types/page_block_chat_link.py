from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatPhotoInfo


@dataclass(kw_only=True)
class PageBlockChatLink(BaseType):
    """
    A link to a chat
    """

    __type__: Literal["pageBlockChatLink"] = "pageBlockChatLink"

    title: str
    """Chat title"""
    photo: ChatPhotoInfo | None = None
    """Chat photo; may be null"""
    accent_color_id: int
    """Identifier of the accent color for chat title and background of chat photo"""
    username: str
    """Chat username by which all other information about the chat can be resolved"""
