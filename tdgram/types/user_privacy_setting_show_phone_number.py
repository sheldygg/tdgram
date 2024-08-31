from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserPrivacySettingShowPhoneNumber(BaseType):
    """
    A privacy setting for managing whether the user's phone number is visible
    """

    __type__: Literal["userPrivacySettingShowPhoneNumber"] = "userPrivacySettingShowPhoneNumber"
