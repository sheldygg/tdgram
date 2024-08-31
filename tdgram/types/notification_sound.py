from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import File


@dataclass(kw_only=True)
class NotificationSound(BaseType):
    """
    Describes a notification sound in MP3 format
    """

    __type__: Literal["notificationSound"] = "notificationSound"

    id: int
    """Unique identifier of the notification sound"""
    duration: int
    """Duration of the sound, in seconds"""
    date: int
    """Point in time (Unix timestamp) when the sound was created"""
    title: str
    """Title of the notification sound"""
    data: str
    """Arbitrary data, defined while the sound was uploaded"""
    sound: File
    """File containing the sound"""
