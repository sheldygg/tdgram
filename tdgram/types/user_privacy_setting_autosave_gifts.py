from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserPrivacySettingAutosaveGifts(BaseType):
    """
    A privacy setting for managing whether received gifts are automatically shown on the user's profile page
    """

    __type__: Literal["userPrivacySettingAutosaveGifts"] = "userPrivacySettingAutosaveGifts"
