from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import SecretChat


@dataclass(kw_only=True)
class UpdateSecretChat(BaseType):
    """
    Some data of a secret chat has changed. This update is guaranteed to come before the secret chat identifier is returned to the application
    """

    __type__: Literal["updateSecretChat"] = "updateSecretChat"

    secret_chat: SecretChat
    """New data about the secret chat"""
