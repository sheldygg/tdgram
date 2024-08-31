from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserPrivacySettingRuleRestrictAll(BaseType):
    """
    A rule to restrict all users from doing something
    """

    __type__: Literal["userPrivacySettingRuleRestrictAll"] = "userPrivacySettingRuleRestrictAll"
