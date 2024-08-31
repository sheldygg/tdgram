from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatActionBar


@dataclass(kw_only=True)
class UpdateChatActionBar(BaseType):
    """
    The chat action bar was changed
    """

    __type__: Literal["updateChatActionBar"] = "updateChatActionBar"

    chat_id: int
    """Chat identifier"""
    action_bar: ChatActionBar | None = None
    """The new value of the action bar; may be null"""
