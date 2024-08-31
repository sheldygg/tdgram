from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatBoostLinkInfo(BaseType):
    """
    Contains information about a link to boost a chat
    """

    __type__: Literal["chatBoostLinkInfo"] = "chatBoostLinkInfo"

    is_public: bool
    """True, if the link will work for non-members of the chat"""
    chat_id: int
    """Identifier of the chat to which the link points; 0 if the chat isn't found"""
