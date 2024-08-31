from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, ReactionNotificationSettings
from .base import BaseMethod


@dataclass(kw_only=True)
class SetReactionNotificationSettings(BaseMethod):
    """
    Changes notification settings for reactions
    """

    __type__: Literal["setReactionNotificationSettings"] = "setReactionNotificationSettings"
    __returning_type__ = Ok

    notification_settings: ReactionNotificationSettings
    """The new notification settings for reactions"""
