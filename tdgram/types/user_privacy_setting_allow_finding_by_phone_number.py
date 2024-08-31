from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserPrivacySettingAllowFindingByPhoneNumber(BaseType):
    """
    A privacy setting for managing whether the user can be found by their phone number. Checked only if the phone number is not known to the other user. Can be set only to 'Allow contacts' or 'Allow all'
    """

    __type__: Literal["userPrivacySettingAllowFindingByPhoneNumber"] = (
        "userPrivacySettingAllowFindingByPhoneNumber"
    )
