from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumFeatureMessagePrivacy(BaseType):
    """
    The ability to disallow incoming voice and video note messages in private chats using setUserPrivacySettingRules with userPrivacySettingAllowPrivateVoiceAndVideoNoteMessages
    """

    __type__: Literal["premiumFeatureMessagePrivacy"] = "premiumFeatureMessagePrivacy"
