from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetBotUpdatesStatus(BaseMethod):
    """
    Informs the server about the number of pending bot updates if they haven't been processed for a long time; for bots only
    """

    __type__: Literal["setBotUpdatesStatus"] = "setBotUpdatesStatus"
    __returning_type__ = Ok

    pending_update_count: int
    """The number of pending updates"""
    error_message: str
    """The last error message"""
