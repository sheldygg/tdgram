from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import GroupCallStreams
from .base import BaseMethod


@dataclass(kw_only=True)
class GetGroupCallStreams(BaseMethod):
    """
    Returns information about available group call streams
    """

    __type__: Literal["getGroupCallStreams"] = "getGroupCallStreams"
    __returning_type__ = GroupCallStreams

    group_call_id: int
    """Group call identifier"""
