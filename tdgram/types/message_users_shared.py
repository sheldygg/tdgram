from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import SharedUser


@dataclass(kw_only=True)
class MessageUsersShared(BaseType):
    """
    The current user shared users, which were requested by the bot
    """

    __type__: Literal["messageUsersShared"] = "messageUsersShared"

    users: list[SharedUser]
    """The shared users"""
    button_id: int
    """Identifier of the keyboard button with the request"""
