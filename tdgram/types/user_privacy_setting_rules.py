from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import UserPrivacySettingRule


@dataclass(kw_only=True)
class UserPrivacySettingRules(BaseType):
    """
    A list of privacy rules. Rules are matched in the specified order. The first matched rule defines the privacy setting for a given user. If no rule matches, the action is not allowed
    """

    __type__: Literal["userPrivacySettingRules"] = "userPrivacySettingRules"

    rules: list[UserPrivacySettingRule]
    """A list of rules"""
