from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class GroupCallId(BaseType):
    """
    Contains the group call identifier
    """

    __type__: Literal["groupCallId"] = "groupCallId"

    id: int
    """Group call identifier"""
