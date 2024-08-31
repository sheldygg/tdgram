from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserStatusEmpty(BaseType):
    """
    The user's status has never been changed
    """

    __type__: Literal["userStatusEmpty"] = "userStatusEmpty"
