from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetChatTitle(BaseMethod):
    """
    Changes the chat title. Supported only for basic groups, supergroups and channels. Requires can_change_info member right
    """

    __type__: Literal["setChatTitle"] = "setChatTitle"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    title: str
    """New title of the chat; 1-128 characters"""
