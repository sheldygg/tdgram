from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import User


@dataclass(kw_only=True)
class UpdateUser(BaseType):
    """
    Some data of a user has changed. This update is guaranteed to come before the user identifier is returned to the application
    """

    __type__: Literal["updateUser"] = "updateUser"

    user: User
    """New data about the user"""
