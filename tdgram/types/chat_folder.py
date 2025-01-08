from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatFolderIcon, ChatFolderName


@dataclass(kw_only=True)
class ChatFolder(BaseType):
    """
    Represents a folder for user chats
    """

    __type__: Literal["chatFolder"] = "chatFolder"

    name: ChatFolderName
    """The name of the folder"""
    icon: ChatFolderIcon | None = None
    """The chosen icon for the chat folder; may be null. If null, use getChatFolderDefaultIconName to get default icon name for the folder"""
    color_id: int
    """The identifier of the chosen color for the chat folder icon; from -1 to 6. If -1, then color is disabled. Can't be changed if folder tags are disabled or the current user doesn't have Telegram Premium subscription"""
    is_shareable: bool
    """True, if at least one link has been created for the folder"""
    pinned_chat_ids: list[int]
    """The chat identifiers of pinned chats in the folder. There can be up to getOption('chat_folder_chosen_chat_count_max') pinned and always included non-secret chats and the same number of secret chats, but the limit can be increased with Telegram Premium"""
    included_chat_ids: list[int]
    """The chat identifiers of always included chats in the folder. There can be up to getOption('chat_folder_chosen_chat_count_max') pinned and always included non-secret chats and the same number of secret chats, but the limit can be increased with Telegram Premium"""
    excluded_chat_ids: list[int]
    """The chat identifiers of always excluded chats in the folder. There can be up to getOption('chat_folder_chosen_chat_count_max') always excluded non-secret chats and the same number of secret chats, but the limit can be increased with Telegram Premium"""
    exclude_muted: bool
    """True, if muted chats need to be excluded"""
    exclude_read: bool
    """True, if read chats need to be excluded"""
    exclude_archived: bool
    """True, if archived chats need to be excluded"""
    include_contacts: bool
    """True, if contacts need to be included"""
    include_non_contacts: bool
    """True, if non-contact users need to be included"""
    include_bots: bool
    """True, if bots need to be included"""
    include_groups: bool
    """True, if basic groups and supergroups need to be included"""
    include_channels: bool
    """True, if channels need to be included"""
