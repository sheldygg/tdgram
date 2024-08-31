from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import AutoDownloadSettingsPresets
from .base import BaseMethod


@dataclass(kw_only=True)
class GetAutoDownloadSettingsPresets(BaseMethod):
    """
    Returns auto-download settings presets for the current user
    """

    __type__: Literal["getAutoDownloadSettingsPresets"] = "getAutoDownloadSettingsPresets"
    __returning_type__ = AutoDownloadSettingsPresets
