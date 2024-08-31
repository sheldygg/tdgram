from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatPermissions


@dataclass(kw_only=True)
class UpdateChatPermissions(BaseType):
    """
    Chat permissions were changed
    """

    __type__: Literal["updateChatPermissions"] = "updateChatPermissions"

    chat_id: int
    """Chat identifier"""
    permissions: ChatPermissions
    """The new chat permissions"""
