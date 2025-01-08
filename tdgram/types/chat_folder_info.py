from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatFolderIcon, ChatFolderName


@dataclass(kw_only=True)
class ChatFolderInfo(BaseType):
    """
    Contains basic information about a chat folder
    """

    __type__: Literal["chatFolderInfo"] = "chatFolderInfo"

    id: int
    """Unique chat folder identifier"""
    name: ChatFolderName
    """The name of the folder"""
    icon: ChatFolderIcon
    """The chosen or default icon for the chat folder"""
    color_id: int
    """The identifier of the chosen color for the chat folder icon; from -1 to 6. If -1, then color is disabled"""
    is_shareable: bool
    """True, if at least one link has been created for the folder"""
    has_my_invite_links: bool
    """True, if the chat folder has invite links created by the current user"""
