from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReadDatePrivacySettings(BaseType):
    """
    Contains privacy settings for message read date in private chats. Read dates are always shown to the users that can see online status of the current user regardless of this setting
    """

    __type__: Literal["readDatePrivacySettings"] = "readDatePrivacySettings"

    show_read_date: bool
    """True, if message read date is shown to other users in private chats. If false and the current user isn't a Telegram Premium user, then they will not be able to see other's message read date"""
