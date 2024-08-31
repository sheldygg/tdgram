from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserPrivacySettingRuleRestrictContacts(BaseType):
    """
    A rule to restrict all contacts of the user from doing something
    """

    __type__: Literal["userPrivacySettingRuleRestrictContacts"] = (
        "userPrivacySettingRuleRestrictContacts"
    )
