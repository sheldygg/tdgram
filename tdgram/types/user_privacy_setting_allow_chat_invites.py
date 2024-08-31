from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserPrivacySettingAllowChatInvites(BaseType):
    """
    A privacy setting for managing whether the user can be invited to chats
    """

    __type__: Literal["userPrivacySettingAllowChatInvites"] = "userPrivacySettingAllowChatInvites"
