from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class NewChatPrivacySettings(BaseType):
    """
    Contains privacy settings for new chats with non-contacts
    """

    __type__: Literal["newChatPrivacySettings"] = "newChatPrivacySettings"

    allow_new_chats_from_unknown_users: bool
    """True, if non-contacts users are able to write first to the current user. Telegram Premium subscribers are able to write first regardless of this setting"""
