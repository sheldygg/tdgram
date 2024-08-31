from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BotMediaPreview, InputStoryContent
from .base import BaseMethod


@dataclass(kw_only=True)
class AddBotMediaPreview(BaseMethod):
    """
    Adds a new media preview to the beginning of the list of media previews of a bot. Returns the added preview after addition is completed server-side. The total number of previews must not exceed getOption('bot_media_preview_count_max') for the given language
    """

    __type__: Literal["addBotMediaPreview"] = "addBotMediaPreview"
    __returning_type__ = BotMediaPreview

    bot_user_id: int
    """Identifier of the target bot. The bot must be owned and must have the main Web App"""
    language_code: str
    """A two-letter ISO 639-1 language code for which preview is added. If empty, then the preview will be shown to all users for whose languages there are no dedicated previews."""
    content: InputStoryContent
    """Content of the added preview"""
