from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import UserPrivacySetting, UserPrivacySettingRules


@dataclass(kw_only=True)
class UpdateUserPrivacySettingRules(BaseType):
    """
    Some privacy setting rules have been changed
    """

    __type__: Literal["updateUserPrivacySettingRules"] = "updateUserPrivacySettingRules"

    setting: UserPrivacySetting
    """The privacy setting"""
    rules: UserPrivacySettingRules
    """New privacy rules"""
