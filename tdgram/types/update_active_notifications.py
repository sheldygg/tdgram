from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import NotificationGroup


@dataclass(kw_only=True)
class UpdateActiveNotifications(BaseType):
    """
    Contains active notifications that were shown on previous application launches. This update is sent only if the message database is used. In that case it comes once before any updateNotification and updateNotificationGroup update
    """

    __type__: Literal["updateActiveNotifications"] = "updateActiveNotifications"

    groups: list[NotificationGroup]
    """Lists of active notification groups"""
