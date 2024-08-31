from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserPrivacySettingShowStatus(BaseType):
    """
    A privacy setting for managing whether the user's online status is visible
    """

    __type__: Literal["userPrivacySettingShowStatus"] = "userPrivacySettingShowStatus"
