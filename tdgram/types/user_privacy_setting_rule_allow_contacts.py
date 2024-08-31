from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserPrivacySettingRuleAllowContacts(BaseType):
    """
    A rule to allow all contacts of the user to do something
    """

    __type__: Literal["userPrivacySettingRuleAllowContacts"] = (
        "userPrivacySettingRuleAllowContacts"
    )
