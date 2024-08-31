from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Birthdate


@dataclass(kw_only=True)
class CloseBirthdayUser(BaseType):
    """
    Describes a user that had or will have a birthday soon
    """

    __type__: Literal["closeBirthdayUser"] = "closeBirthdayUser"

    user_id: int
    """User identifier"""
    birthdate: Birthdate
    """Birthdate of the user"""
