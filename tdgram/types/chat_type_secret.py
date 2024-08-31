from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatTypeSecret(BaseType):
    """
    A secret chat with a user
    """

    __type__: Literal["chatTypeSecret"] = "chatTypeSecret"

    secret_chat_id: int
    """Secret chat identifier"""
    user_id: int
    """User identifier of the other user in the secret chat"""
