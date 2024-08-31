from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import SecretChat
from .base import BaseMethod


@dataclass(kw_only=True)
class GetSecretChat(BaseMethod):
    """
    Returns information about a secret chat by its identifier. This is an offline request
    """

    __type__: Literal["getSecretChat"] = "getSecretChat"
    __returning_type__ = SecretChat

    secret_chat_id: int
    """Secret chat identifier"""
