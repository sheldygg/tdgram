from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ActivateStoryStealthMode(BaseMethod):
    """
    Activates stealth mode for stories, which hides all views of stories from the current user in the last 'story_stealth_mode_past_period' seconds
    """

    __type__: Literal["activateStoryStealthMode"] = "activateStoryStealthMode"
    __returning_type__ = Ok
