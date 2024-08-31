from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserTypeRegular(BaseType):
    """
    A regular user
    """

    __type__: Literal["userTypeRegular"] = "userTypeRegular"
