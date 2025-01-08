from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserPrivacySettingRuleRestrictBots(BaseType):
    """
    A rule to restrict all bots from doing something
    """

    __type__: Literal["userPrivacySettingRuleRestrictBots"] = "userPrivacySettingRuleRestrictBots"
