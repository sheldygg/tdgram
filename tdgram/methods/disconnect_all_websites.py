from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DisconnectAllWebsites(BaseMethod):
    """
    Disconnects all websites from the current user's Telegram account
    """

    __type__: Literal["disconnectAllWebsites"] = "disconnectAllWebsites"
    __returning_type__ = Ok
