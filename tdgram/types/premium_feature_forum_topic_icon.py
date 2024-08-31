from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumFeatureForumTopicIcon(BaseType):
    """
    The ability to set a custom emoji as a forum topic icon
    """

    __type__: Literal["premiumFeatureForumTopicIcon"] = "premiumFeatureForumTopicIcon"
