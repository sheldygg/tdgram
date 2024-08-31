from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ConnectedWebsites
from .base import BaseMethod


@dataclass(kw_only=True)
class GetConnectedWebsites(BaseMethod):
    """
    Returns all website where the current user used Telegram to log in
    """

    __type__: Literal["getConnectedWebsites"] = "getConnectedWebsites"
    __returning_type__ = ConnectedWebsites
