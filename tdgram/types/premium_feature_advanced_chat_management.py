from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumFeatureAdvancedChatManagement(BaseType):
    """
    Ability to change position of the main chat list, archive and mute all new chats from non-contacts, and completely disable notifications about the user's contacts joined Telegram
    """

    __type__: Literal["premiumFeatureAdvancedChatManagement"] = (
        "premiumFeatureAdvancedChatManagement"
    )
