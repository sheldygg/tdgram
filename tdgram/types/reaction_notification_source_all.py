from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReactionNotificationSourceAll(BaseType):
    """
    Notifications for reactions are shown for all reactions
    """

    __type__: Literal["reactionNotificationSourceAll"] = "reactionNotificationSourceAll"
