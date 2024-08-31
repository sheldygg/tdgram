from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetInlineGameScore(BaseMethod):
    """
    Updates the game score of the specified user in a game; for bots only
    """

    __type__: Literal["setInlineGameScore"] = "setInlineGameScore"
    __returning_type__ = Ok

    inline_message_id: str
    """Inline message identifier"""
    edit_message: bool
    """Pass true to edit the game message to include the current scoreboard"""
    user_id: int
    """User identifier"""
    score: int
    """The new score"""
    force: bool
    """Pass true to update the score even if it decreases. If the score is 0, the user will be deleted from the high score table"""
