from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserPrivacySettingAllowCalls(BaseType):
    """
    A privacy setting for managing whether the user can be called
    """

    __type__: Literal["userPrivacySettingAllowCalls"] = "userPrivacySettingAllowCalls"
