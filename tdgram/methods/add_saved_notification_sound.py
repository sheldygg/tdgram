from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputFile, NotificationSound
from .base import BaseMethod


@dataclass(kw_only=True)
class AddSavedNotificationSound(BaseMethod):
    """
    Adds a new notification sound to the list of saved notification sounds. The new notification sound is added to the top of the list. If it is already in the list, its position isn't changed
    """

    __type__: Literal["addSavedNotificationSound"] = "addSavedNotificationSound"
    __returning_type__ = NotificationSound

    sound: InputFile
    """Notification sound file to add"""
