from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BotMediaPreview, InputStoryContent
from .base import BaseMethod


@dataclass(kw_only=True)
class EditBotMediaPreview(BaseMethod):
    """
    Replaces media preview in the list of media previews of a bot. Returns the new preview after edit is completed server-side
    """

    __type__: Literal["editBotMediaPreview"] = "editBotMediaPreview"
    __returning_type__ = BotMediaPreview

    bot_user_id: int
    """Identifier of the target bot. The bot must be owned and must have the main Web App"""
    language_code: str
    """Language code of the media preview to edit"""
    file_id: int
    """File identifier of the media to replace"""
    content: InputStoryContent
    """Content of the new preview"""
