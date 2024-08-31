from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserPrivacySettingRuleAllowUsers(BaseType):
    """
    A rule to allow certain specified users to do something
    """

    __type__: Literal["userPrivacySettingRuleAllowUsers"] = "userPrivacySettingRuleAllowUsers"

    user_ids: list[int]
    """The user identifiers, total number of users in all rules must not exceed 1000"""
