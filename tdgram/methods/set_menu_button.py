from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BotMenuButton, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetMenuButton(BaseMethod):
    """
    Sets menu button for the given user or for all users; for bots only
    """

    __type__: Literal["setMenuButton"] = "setMenuButton"
    __returning_type__ = Ok

    user_id: int
    """Identifier of the user or 0 to set menu button for all users"""
    menu_button: BotMenuButton
    """New menu button"""
