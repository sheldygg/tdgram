from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetGroupCallTitle(BaseMethod):
    """
    Sets group call title. Requires groupCall.can_be_managed group call flag
    """

    __type__: Literal["setGroupCallTitle"] = "setGroupCallTitle"
    __returning_type__ = Ok

    group_call_id: int
    """Group call identifier"""
    title: str
    """New group call title; 1-64 characters"""
