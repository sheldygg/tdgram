from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateChatIsTranslatable(BaseType):
    """
    Translation of chat messages was enabled or disabled
    """

    __type__: Literal["updateChatIsTranslatable"] = "updateChatIsTranslatable"

    chat_id: int
    """Chat identifier"""
    is_translatable: bool
    """New value of is_translatable"""
