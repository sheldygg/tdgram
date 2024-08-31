from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BotMenuButton
from .base import BaseMethod


@dataclass(kw_only=True)
class GetMenuButton(BaseMethod):
    """
    Returns menu button set by the bot for the given user; for bots only
    """

    __type__: Literal["getMenuButton"] = "getMenuButton"
    __returning_type__ = BotMenuButton

    user_id: int
    """Identifier of the user or 0 to get the default menu button"""
