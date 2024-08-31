from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RevokeGroupCallInviteLink(BaseMethod):
    """
    Revokes invite link for a group call. Requires groupCall.can_be_managed group call flag
    """

    __type__: Literal["revokeGroupCallInviteLink"] = "revokeGroupCallInviteLink"
    __returning_type__ = Ok

    group_call_id: int
    """Group call identifier"""
