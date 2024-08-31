from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Photo


@dataclass(kw_only=True)
class SharedUser(BaseType):
    """
    Contains information about a user shared with a bot
    """

    __type__: Literal["sharedUser"] = "sharedUser"

    user_id: int
    """User identifier"""
    first_name: str
    """First name of the user; for bots only"""
    last_name: str
    """Last name of the user; for bots only"""
    username: str
    """Username of the user; for bots only"""
    photo: Photo | None = None
    """Profile photo of the user; for bots only; may be null"""
