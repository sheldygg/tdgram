from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import CloseBirthdayUser


@dataclass(kw_only=True)
class UpdateContactCloseBirthdays(BaseType):
    """
    The list of contacts that had birthdays recently or will have birthday soon has changed
    """

    __type__: Literal["updateContactCloseBirthdays"] = "updateContactCloseBirthdays"

    close_birthday_users: list[CloseBirthdayUser]
    """List of contact users with close birthday"""
