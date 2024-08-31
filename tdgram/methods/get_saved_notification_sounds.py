from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import NotificationSounds
from .base import BaseMethod


@dataclass(kw_only=True)
class GetSavedNotificationSounds(BaseMethod):
    """
    Returns the list of saved notification sounds. If a sound isn't in the list, then default sound needs to be used
    """

    __type__: Literal["getSavedNotificationSounds"] = "getSavedNotificationSounds"
    __returning_type__ = NotificationSounds
