from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatEventSlowModeDelayChanged(BaseType):
    """
    The slow_mode_delay setting of a supergroup was changed
    """

    __type__: Literal["chatEventSlowModeDelayChanged"] = "chatEventSlowModeDelayChanged"

    old_slow_mode_delay: int
    """Previous value of slow_mode_delay, in seconds"""
    new_slow_mode_delay: int
    """New value of slow_mode_delay, in seconds"""
