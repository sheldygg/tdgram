from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteBotMediaPreviews(BaseMethod):
    """
    Delete media previews from the list of media previews of a bot
    """

    __type__: Literal["deleteBotMediaPreviews"] = "deleteBotMediaPreviews"
    __returning_type__ = Ok

    bot_user_id: int
    """Identifier of the target bot. The bot must be owned and must have the main Web App"""
    language_code: str
    """Language code of the media previews to delete"""
    file_ids: list[int]
    """File identifiers of the media to delete"""
