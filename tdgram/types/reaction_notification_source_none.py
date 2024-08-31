from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReactionNotificationSourceNone(BaseType):
    """
    Notifications for reactions are disabled
    """

    __type__: Literal["reactionNotificationSourceNone"] = "reactionNotificationSourceNone"
