from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Chat


@dataclass(kw_only=True)
class UpdateNewChat(BaseType):
    """
    A new chat has been loaded/created. This update is guaranteed to come before the chat identifier is returned to the application. The chat field changes will be reported through separate updates
    """

    __type__: Literal["updateNewChat"] = "updateNewChat"

    chat: Chat
    """The chat"""
