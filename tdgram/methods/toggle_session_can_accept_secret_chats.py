from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleSessionCanAcceptSecretChats(BaseMethod):
    """
    Toggles whether a session can accept incoming secret chats
    """

    __type__: Literal["toggleSessionCanAcceptSecretChats"] = "toggleSessionCanAcceptSecretChats"
    __returning_type__ = Ok

    session_id: int
    """Session identifier"""
    can_accept_secret_chats: bool
    """Pass true to allow accepting secret chats by the session; pass false otherwise"""
