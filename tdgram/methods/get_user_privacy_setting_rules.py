from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import UserPrivacySetting, UserPrivacySettingRules
from .base import BaseMethod


@dataclass(kw_only=True)
class GetUserPrivacySettingRules(BaseMethod):
    """
    Returns the current privacy settings
    """

    __type__: Literal["getUserPrivacySettingRules"] = "getUserPrivacySettingRules"
    __returning_type__ = UserPrivacySettingRules

    setting: UserPrivacySetting
    """The privacy setting"""
