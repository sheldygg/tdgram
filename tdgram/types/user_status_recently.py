from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserStatusRecently(BaseType):
    """
    The user was online recently
    """

    __type__: Literal["userStatusRecently"] = "userStatusRecently"

    by_my_privacy_settings: bool
    """Exact user's status is hidden because the current user enabled userPrivacySettingShowStatus privacy setting for the user and has no Telegram Premium"""
