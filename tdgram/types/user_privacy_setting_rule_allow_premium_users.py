from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserPrivacySettingRuleAllowPremiumUsers(BaseType):
    """
    A rule to allow all Premium Users to do something; currently, allowed only for userPrivacySettingAllowChatInvites
    """

    __type__: Literal["userPrivacySettingRuleAllowPremiumUsers"] = (
        "userPrivacySettingRuleAllowPremiumUsers"
    )
