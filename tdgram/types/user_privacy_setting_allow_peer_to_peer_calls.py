from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserPrivacySettingAllowPeerToPeerCalls(BaseType):
    """
    A privacy setting for managing whether peer-to-peer connections can be used for calls
    """

    __type__: Literal["userPrivacySettingAllowPeerToPeerCalls"] = (
        "userPrivacySettingAllowPeerToPeerCalls"
    )
