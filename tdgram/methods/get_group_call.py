from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import GroupCall
from .base import BaseMethod


@dataclass(kw_only=True)
class GetGroupCall(BaseMethod):
    """
    Returns information about a group call
    """

    __type__: Literal["getGroupCall"] = "getGroupCall"
    __returning_type__ = GroupCall

    group_call_id: int
    """Group call identifier"""
