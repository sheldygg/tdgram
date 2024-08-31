from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ScopeAutosaveSettings(BaseType):
    """
    Contains autosave settings for an autosave settings scope
    """

    __type__: Literal["scopeAutosaveSettings"] = "scopeAutosaveSettings"

    autosave_photos: bool
    """True, if photo autosave is enabled"""
    autosave_videos: bool
    """True, if video autosave is enabled"""
    max_video_file_size: int
    """The maximum size of a video file to be autosaved, in bytes; 512 KB - 4000 MB"""
