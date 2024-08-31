from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BusinessBotManageBar


@dataclass(kw_only=True)
class UpdateChatBusinessBotManageBar(BaseType):
    """
    The bar for managing business bot was changed in a chat
    """

    __type__: Literal["updateChatBusinessBotManageBar"] = "updateChatBusinessBotManageBar"

    chat_id: int
    """Chat identifier"""
    business_bot_manage_bar: BusinessBotManageBar | None = None
    """The new value of the business bot manage bar; may be null"""
