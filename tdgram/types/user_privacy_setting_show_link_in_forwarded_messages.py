from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserPrivacySettingShowLinkInForwardedMessages(BaseType):
    """
    A privacy setting for managing whether a link to the user's account is included in forwarded messages
    """

    __type__: Literal["userPrivacySettingShowLinkInForwardedMessages"] = (
        "userPrivacySettingShowLinkInForwardedMessages"
    )
