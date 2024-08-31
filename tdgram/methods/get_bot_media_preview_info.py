from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BotMediaPreviewInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class GetBotMediaPreviewInfo(BaseMethod):
    """
    Returns the list of media previews for the given language and the list of languages for which the bot has dedicated previews
    """

    __type__: Literal["getBotMediaPreviewInfo"] = "getBotMediaPreviewInfo"
    __returning_type__ = BotMediaPreviewInfo

    bot_user_id: int
    """Identifier of the target bot. The bot must be owned and must have the main Web App"""
    language_code: str
    """A two-letter ISO 639-1 language code for which to get previews. If empty, then default previews are returned"""
