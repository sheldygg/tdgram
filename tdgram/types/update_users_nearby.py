from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatNearby


@dataclass(kw_only=True)
class UpdateUsersNearby(BaseType):
    """
    The list of users nearby has changed. The update is guaranteed to be sent only 60 seconds after a successful searchChatsNearby request
    """

    __type__: Literal["updateUsersNearby"] = "updateUsersNearby"

    users_nearby: list[ChatNearby]
    """The new list of users nearby"""
