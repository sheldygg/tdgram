from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserPrivacySettingShowProfilePhoto(BaseType):
    """
    A privacy setting for managing whether the user's profile photo is visible
    """

    __type__: Literal["userPrivacySettingShowProfilePhoto"] = "userPrivacySettingShowProfilePhoto"
