from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleDownloadIsPaused(BaseMethod):
    """
    Changes pause state of a file in the file download list
    """

    __type__: Literal["toggleDownloadIsPaused"] = "toggleDownloadIsPaused"
    __returning_type__ = Ok

    file_id: int
    """Identifier of the downloaded file"""
    is_paused: bool
    """Pass true if the download is paused"""
