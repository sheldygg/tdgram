from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class OpenChat(BaseMethod):
    """
    Informs TDLib that the chat is opened by the user. Many useful activities depend on the chat being opened or closed (e.g., in supergroups and channels all updates are received only for opened chats)
    """

    __type__: Literal["openChat"] = "openChat"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
