from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumLimitTypeChatFolderChosenChatCount(BaseType):
    """
    The maximum number of pinned and always included, or always excluded chats in a chat folder
    """

    __type__: Literal["premiumLimitTypeChatFolderChosenChatCount"] = (
        "premiumLimitTypeChatFolderChosenChatCount"
    )
