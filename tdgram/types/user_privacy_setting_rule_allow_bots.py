from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserPrivacySettingRuleAllowBots(BaseType):
    """
    A rule to allow all bots to do something
    """

    __type__: Literal["userPrivacySettingRuleAllowBots"] = "userPrivacySettingRuleAllowBots"
