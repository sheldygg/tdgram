from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleChatIsTranslatable(BaseMethod):
    """
    Changes the translatable state of a chat
    """

    __type__: Literal["toggleChatIsTranslatable"] = "toggleChatIsTranslatable"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    is_translatable: bool
    """New value of is_translatable"""
