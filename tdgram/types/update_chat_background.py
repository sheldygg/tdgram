from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatBackground


@dataclass(kw_only=True)
class UpdateChatBackground(BaseType):
    """
    The chat background was changed
    """

    __type__: Literal["updateChatBackground"] = "updateChatBackground"

    chat_id: int
    """Chat identifier"""
    background: ChatBackground | None = None
    """The new chat background; may be null if background was reset to default"""
