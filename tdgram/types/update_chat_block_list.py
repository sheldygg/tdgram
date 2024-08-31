from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BlockList


@dataclass(kw_only=True)
class UpdateChatBlockList(BaseType):
    """
    A chat was blocked or unblocked
    """

    __type__: Literal["updateChatBlockList"] = "updateChatBlockList"

    chat_id: int
    """Chat identifier"""
    block_list: BlockList | None = None
    """Block list to which the chat is added; may be null if none"""
