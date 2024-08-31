from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chat
from .base import BaseMethod


@dataclass(kw_only=True)
class CreateNewSecretChat(BaseMethod):
    """
    Creates a new secret chat. Returns the newly created chat
    """

    __type__: Literal["createNewSecretChat"] = "createNewSecretChat"
    __returning_type__ = Chat

    user_id: int
    """Identifier of the target user"""
