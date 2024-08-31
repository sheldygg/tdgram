from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import NotificationSound


@dataclass(kw_only=True)
class NotificationSounds(BaseType):
    """
    Contains a list of notification sounds
    """

    __type__: Literal["notificationSounds"] = "notificationSounds"

    notification_sounds: list[NotificationSound]
    """A list of notification sounds"""
