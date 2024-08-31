from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleHasSponsoredMessagesEnabled(BaseMethod):
    """
    Toggles whether the current user has sponsored messages enabled. The setting has no effect for users without Telegram Premium for which sponsored messages are always enabled
    """

    __type__: Literal["toggleHasSponsoredMessagesEnabled"] = "toggleHasSponsoredMessagesEnabled"
    __returning_type__ = Ok

    has_sponsored_messages_enabled: bool
    """Pass true to enable sponsored messages for the current user; false to disable them"""
