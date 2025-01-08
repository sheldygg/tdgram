from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Gift


@dataclass(kw_only=True)
class Gifts(BaseType):
    """
    Contains a list of gifts that can be sent to another user
    """

    __type__: Literal["gifts"] = "gifts"

    gifts: list[Gift]
    """The list of gifts"""
