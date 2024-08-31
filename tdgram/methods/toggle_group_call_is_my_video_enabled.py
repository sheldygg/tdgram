from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleGroupCallIsMyVideoEnabled(BaseMethod):
    """
    Toggles whether current user's video is enabled
    """

    __type__: Literal["toggleGroupCallIsMyVideoEnabled"] = "toggleGroupCallIsMyVideoEnabled"
    __returning_type__ = Ok

    group_call_id: int
    """Group call identifier"""
    is_my_video_enabled: bool
    """Pass true if the current user's video is enabled"""
