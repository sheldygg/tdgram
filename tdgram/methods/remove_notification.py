from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RemoveNotification(BaseMethod):
    """
    Removes an active notification from notification list. Needs to be called only if the notification is removed by the current user
    """

    __type__: Literal["removeNotification"] = "removeNotification"
    __returning_type__ = Ok

    notification_group_id: int
    """Identifier of notification group to which the notification belongs"""
    notification_id: int
    """Identifier of removed notification"""
