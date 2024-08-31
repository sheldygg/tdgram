from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleBusinessConnectedBotChatIsPaused(BaseMethod):
    """
    Pauses or resumes the connected business bot in a specific chat
    """

    __type__: Literal["toggleBusinessConnectedBotChatIsPaused"] = (
        "toggleBusinessConnectedBotChatIsPaused"
    )
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    is_paused: bool
    """Pass true to pause the connected bot in the chat; pass false to resume the bot"""
