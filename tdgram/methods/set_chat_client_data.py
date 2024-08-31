from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetChatClientData(BaseMethod):
    """
    Changes application-specific data associated with a chat
    """

    __type__: Literal["setChatClientData"] = "setChatClientData"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    client_data: str
    """New value of client_data"""
