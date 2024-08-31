from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ResetAllNotificationSettings(BaseMethod):
    """
    Resets all chat and scope notification settings to their default values. By default, all chats are unmuted and message previews are shown
    """

    __type__: Literal["resetAllNotificationSettings"] = "resetAllNotificationSettings"
    __returning_type__ = Ok
