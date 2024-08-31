from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateSavedNotificationSounds(BaseType):
    """
    The list of saved notification sounds was updated. This update may not be sent until information about a notification sound was requested for the first time
    """

    __type__: Literal["updateSavedNotificationSounds"] = "updateSavedNotificationSounds"

    notification_sound_ids: list[int]
    """The new list of identifiers of saved notification sounds"""
