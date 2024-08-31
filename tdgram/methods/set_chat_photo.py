from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputChatPhoto, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetChatPhoto(BaseMethod):
    """
    Changes the photo of a chat. Supported only for basic groups, supergroups and channels. Requires can_change_info member right
    """

    __type__: Literal["setChatPhoto"] = "setChatPhoto"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    photo: InputChatPhoto | None = None
    """New chat photo; pass null to delete the chat photo"""
