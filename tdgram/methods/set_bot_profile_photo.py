from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputChatPhoto, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetBotProfilePhoto(BaseMethod):
    """
    Changes a profile photo for a bot
    """

    __type__: Literal["setBotProfilePhoto"] = "setBotProfilePhoto"
    __returning_type__ = Ok

    bot_user_id: int
    """Identifier of the target bot"""
    photo: InputChatPhoto | None = None
    """Profile photo to set; pass null to delete the chat photo"""
