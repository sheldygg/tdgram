from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RemoveNotificationGroup(BaseMethod):
    """
    Removes a group of active notifications. Needs to be called only if the notification group is removed by the current user
    """

    __type__: Literal["removeNotificationGroup"] = "removeNotificationGroup"
    __returning_type__ = Ok

    notification_group_id: int
    """Notification group identifier"""
    max_notification_id: int
    """The maximum identifier of removed notifications"""
