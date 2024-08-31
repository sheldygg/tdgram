from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ReactionNotificationSettings


@dataclass(kw_only=True)
class UpdateReactionNotificationSettings(BaseType):
    """
    Notification settings for reactions were updated
    """

    __type__: Literal["updateReactionNotificationSettings"] = "updateReactionNotificationSettings"

    notification_settings: ReactionNotificationSettings
    """The new notification settings"""
