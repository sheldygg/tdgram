from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chat
from .base import BaseMethod


@dataclass(kw_only=True)
class CreatePrivateChat(BaseMethod):
    """
    Returns an existing chat corresponding to a given user
    """

    __type__: Literal["createPrivateChat"] = "createPrivateChat"
    __returning_type__ = Chat

    user_id: int
    """User identifier"""
    force: bool
    """Pass true to create the chat without a network request. In this case all information about the chat except its type, title and photo can be incorrect"""
