from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleGroupCallEnabledStartNotification(BaseMethod):
    """
    Toggles whether the current user will receive a notification when the group call starts; scheduled group calls only
    """

    __type__: Literal["toggleGroupCallEnabledStartNotification"] = (
        "toggleGroupCallEnabledStartNotification"
    )
    __returning_type__ = Ok

    group_call_id: int
    """Group call identifier"""
    enabled_start_notification: bool
    """New value of the enabled_start_notification setting"""
