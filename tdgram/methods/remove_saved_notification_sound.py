from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RemoveSavedNotificationSound(BaseMethod):
    """
    Removes a notification sound from the list of saved notification sounds
    """

    __type__: Literal["removeSavedNotificationSound"] = "removeSavedNotificationSound"
    __returning_type__ = Ok

    notification_sound_id: int
    """Identifier of the notification sound"""
