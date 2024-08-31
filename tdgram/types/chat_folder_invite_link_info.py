from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatFolderInfo


@dataclass(kw_only=True)
class ChatFolderInviteLinkInfo(BaseType):
    """
    Contains information about an invite link to a chat folder
    """

    __type__: Literal["chatFolderInviteLinkInfo"] = "chatFolderInviteLinkInfo"

    chat_folder_info: ChatFolderInfo
    """Basic information about the chat folder; chat folder identifier will be 0 if the user didn't have the chat folder yet"""
    missing_chat_ids: list[int]
    """Identifiers of the chats from the link, which aren't added to the folder yet"""
    added_chat_ids: list[int]
    """Identifiers of the chats from the link, which are added to the folder already"""
