from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import NotificationSounds
from .base import BaseMethod


@dataclass(kw_only=True)
class GetSavedNotificationSound(BaseMethod):
    """
    Returns saved notification sound by its identifier. Returns a 404 error if there is no saved notification sound with the specified identifier
    """

    __type__: Literal["getSavedNotificationSound"] = "getSavedNotificationSound"
    __returning_type__ = NotificationSounds

    notification_sound_id: int
    """Identifier of the notification sound"""
