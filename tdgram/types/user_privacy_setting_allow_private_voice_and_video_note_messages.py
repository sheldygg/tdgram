from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserPrivacySettingAllowPrivateVoiceAndVideoNoteMessages(BaseType):
    """
    A privacy setting for managing whether the user can receive voice and video messages in private chats; for Telegram Premium users only
    """

    __type__: Literal["userPrivacySettingAllowPrivateVoiceAndVideoNoteMessages"] = (
        "userPrivacySettingAllowPrivateVoiceAndVideoNoteMessages"
    )
