from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class CloseSecretChat(BaseMethod):
    """
    Closes a secret chat, effectively transferring its state to secretChatStateClosed
    """

    __type__: Literal["closeSecretChat"] = "closeSecretChat"
    __returning_type__ = Ok

    secret_chat_id: int
    """Secret chat identifier"""
