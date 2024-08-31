from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class CloseChat(BaseMethod):
    """
    Informs TDLib that the chat is closed by the user. Many useful activities depend on the chat being opened or closed
    """

    __type__: Literal["closeChat"] = "closeChat"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
