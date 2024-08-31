from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import AutoDownloadSettings, NetworkType, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetAutoDownloadSettings(BaseMethod):
    """
    Sets auto-download settings
    """

    __type__: Literal["setAutoDownloadSettings"] = "setAutoDownloadSettings"
    __returning_type__ = Ok

    settings: AutoDownloadSettings
    """New user auto-download settings"""
    type: NetworkType
    """Type of the network for which the new settings are relevant"""
