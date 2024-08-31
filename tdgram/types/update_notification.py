from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Notification


@dataclass(kw_only=True)
class UpdateNotification(BaseType):
    """
    A notification was changed
    """

    __type__: Literal["updateNotification"] = "updateNotification"

    notification_group_id: int
    """Unique notification group identifier"""
    notification: Notification
    """Changed notification"""
