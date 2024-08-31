from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateStoryStealthMode(BaseType):
    """
    Story stealth mode settings have changed
    """

    __type__: Literal["updateStoryStealthMode"] = "updateStoryStealthMode"

    active_until_date: int
    """Point in time (Unix timestamp) until stealth mode is active; 0 if it is disabled"""
    cooldown_until_date: int
    """Point in time (Unix timestamp) when stealth mode can be enabled again; 0 if there is no active cooldown"""
