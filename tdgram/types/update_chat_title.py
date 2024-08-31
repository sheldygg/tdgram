from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateChatTitle(BaseType):
    """
    The title of a chat was changed
    """

    __type__: Literal["updateChatTitle"] = "updateChatTitle"

    chat_id: int
    """Chat identifier"""
    title: str
    """The new chat title"""
