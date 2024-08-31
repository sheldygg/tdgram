from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BotMediaPreviews
from .base import BaseMethod


@dataclass(kw_only=True)
class GetBotMediaPreviews(BaseMethod):
    """
    Returns the list of media previews of a bot
    """

    __type__: Literal["getBotMediaPreviews"] = "getBotMediaPreviews"
    __returning_type__ = BotMediaPreviews

    bot_user_id: int
    """Identifier of the target bot. The bot must have the main Web App"""
