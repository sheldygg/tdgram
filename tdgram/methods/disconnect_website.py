from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DisconnectWebsite(BaseMethod):
    """
    Disconnects website from the current user's Telegram account
    """

    __type__: Literal["disconnectWebsite"] = "disconnectWebsite"
    __returning_type__ = Ok

    website_id: int
    """Website identifier"""
