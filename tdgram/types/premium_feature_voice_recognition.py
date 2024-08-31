from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumFeatureVoiceRecognition(BaseType):
    """
    The ability to convert voice notes to text
    """

    __type__: Literal["premiumFeatureVoiceRecognition"] = "premiumFeatureVoiceRecognition"
