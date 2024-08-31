from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Message
from .base import BaseMethod


@dataclass(kw_only=True)
class SetGameScore(BaseMethod):
    """
    Updates the game score of the specified user in the game; for bots only
    """

    __type__: Literal["setGameScore"] = "setGameScore"
    __returning_type__ = Message

    chat_id: int
    """The chat to which the message with the game belongs"""
    message_id: int
    """Identifier of the message"""
    edit_message: bool
    """Pass true to edit the game message to include the current scoreboard"""
    user_id: int
    """User identifier"""
    score: int
    """The new score"""
    force: bool
    """Pass true to update the score even if it decreases. If the score is 0, the user will be deleted from the high score table"""
