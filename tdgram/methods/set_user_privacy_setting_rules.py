from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, UserPrivacySetting, UserPrivacySettingRules
from .base import BaseMethod


@dataclass(kw_only=True)
class SetUserPrivacySettingRules(BaseMethod):
    """
    Changes user privacy settings
    """

    __type__: Literal["setUserPrivacySettingRules"] = "setUserPrivacySettingRules"
    __returning_type__ = Ok

    setting: UserPrivacySetting
    """The privacy setting"""
    rules: UserPrivacySettingRules
    """The new privacy rules"""
