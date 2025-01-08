from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import AutoDownloadSettings


@dataclass(kw_only=True)
class AutoDownloadSettingsPresets(BaseType):
    """
    Contains auto-download settings presets for the current user
    """

    __type__: Literal["autoDownloadSettingsPresets"] = "autoDownloadSettingsPresets"

    low: AutoDownloadSettings
    """Preset with lowest settings; expected to be used by default when roaming"""
    medium: AutoDownloadSettings
    """Preset with medium settings; expected to be used by default when using mobile data"""
    high: AutoDownloadSettings
    """Preset with highest settings; expected to be used by default when connected on Wi-Fi"""
