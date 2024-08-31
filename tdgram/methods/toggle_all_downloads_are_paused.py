from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleAllDownloadsArePaused(BaseMethod):
    """
    Changes pause state of all files in the file download list
    """

    __type__: Literal["toggleAllDownloadsArePaused"] = "toggleAllDownloadsArePaused"
    __returning_type__ = Ok

    are_paused: bool
    """Pass true to pause all downloads; pass false to unpause them"""
