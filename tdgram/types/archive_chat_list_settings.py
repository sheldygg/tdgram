from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ArchiveChatListSettings(BaseType):
    """
    Contains settings for automatic moving of chats to and from the Archive chat lists
    """

    __type__: Literal["archiveChatListSettings"] = "archiveChatListSettings"

    archive_and_mute_new_chats_from_unknown_users: bool
    """True, if new chats from non-contacts will be automatically archived and muted. Can be set to true only if the option 'can_archive_and_mute_new_chats_from_unknown_users' is true"""
    keep_unmuted_chats_archived: bool
    """True, if unmuted chats will be kept in the Archive chat list when they get a new message"""
    keep_chats_from_folders_archived: bool
    """True, if unmuted chats, that are always included or pinned in a folder, will be kept in the Archive chat list when they get a new message. Ignored if keep_unmuted_chats_archived == true"""
