from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chat
from .base import BaseMethod


@dataclass(kw_only=True)
class CreateSecretChat(BaseMethod):
    """
    Returns an existing chat corresponding to a known secret chat
    """

    __type__: Literal["createSecretChat"] = "createSecretChat"
    __returning_type__ = Chat

    secret_chat_id: int
    """Secret chat identifier"""
