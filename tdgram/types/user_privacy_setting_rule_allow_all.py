from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserPrivacySettingRuleAllowAll(BaseType):
    """
    A rule to allow all users to do something
    """

    __type__: Literal["userPrivacySettingRuleAllowAll"] = "userPrivacySettingRuleAllowAll"
