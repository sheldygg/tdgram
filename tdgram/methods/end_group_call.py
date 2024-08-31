from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class EndGroupCall(BaseMethod):
    """
    Ends a group call. Requires groupCall.can_be_managed
    """

    __type__: Literal["endGroupCall"] = "endGroupCall"
    __returning_type__ = Ok

    group_call_id: int
    """Group call identifier"""
