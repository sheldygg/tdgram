from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SuggestedActionEnableArchiveAndMuteNewChats(BaseType):
    """
    Suggests the user to enable archive_and_mute_new_chats_from_unknown_users setting in archiveChatListSettings
    """

    __type__: Literal["suggestedActionEnableArchiveAndMuteNewChats"] = (
        "suggestedActionEnableArchiveAndMuteNewChats"
    )
