from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText


@dataclass(kw_only=True)
class UserSupportInfo(BaseType):
    """
    Contains custom information about the user
    """

    __type__: Literal["userSupportInfo"] = "userSupportInfo"

    message: FormattedText
    """Information message"""
    author: str
    """Information author"""
    date: int
    """Information change date"""
