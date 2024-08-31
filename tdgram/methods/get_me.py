from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import User
from .base import BaseMethod


@dataclass(kw_only=True)
class GetMe(BaseMethod):
    """
    Returns the current user
    """

    __type__: Literal["getMe"] = "getMe"
    __returning_type__ = User
