from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatAdministrator(BaseType):
    """
    Contains information about a chat administrator
    """

    __type__: Literal["chatAdministrator"] = "chatAdministrator"

    user_id: int
    """User identifier of the administrator"""
    custom_title: str
    """Custom title of the administrator"""
    is_owner: bool
    """True, if the user is the owner of the chat"""
