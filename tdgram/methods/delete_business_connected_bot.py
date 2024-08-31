from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteBusinessConnectedBot(BaseMethod):
    """
    Deletes the business bot that is connected to the current user account
    """

    __type__: Literal["deleteBusinessConnectedBot"] = "deleteBusinessConnectedBot"
    __returning_type__ = Ok

    bot_user_id: int
    """Unique user identifier for the bot"""
