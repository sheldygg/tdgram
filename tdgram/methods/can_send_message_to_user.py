from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import CanSendMessageToUserResult
from .base import BaseMethod


@dataclass(kw_only=True)
class CanSendMessageToUser(BaseMethod):
    """
    Check whether the current user can message another user or try to create a chat with them
    """

    __type__: Literal["canSendMessageToUser"] = "canSendMessageToUser"
    __returning_type__ = CanSendMessageToUserResult

    user_id: int
    """Identifier of the other user"""
    only_local: bool
    """Pass true to get only locally available information without sending network requests"""
