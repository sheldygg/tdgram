from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FoundUsers
from .base import BaseMethod


@dataclass(kw_only=True)
class GetGrossingWebAppBots(BaseMethod):
    """
    Returns the most grossing Web App bots
    """

    __type__: Literal["getGrossingWebAppBots"] = "getGrossingWebAppBots"
    __returning_type__ = FoundUsers

    offset: str
    """Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results"""
    limit: int
    """The maximum number of bots to be returned; up to 100"""
