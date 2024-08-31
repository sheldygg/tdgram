from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class LoadGroupCallParticipants(BaseMethod):
    """
    Loads more participants of a group call. The loaded participants will be received through updates. Use the field groupCall.loaded_all_participants to check whether all participants have already been loaded
    """

    __type__: Literal["loadGroupCallParticipants"] = "loadGroupCallParticipants"
    __returning_type__ = Ok

    group_call_id: int
    """Group call identifier. The group call must be previously received through getGroupCall and must be joined or being joined"""
    limit: int
    """The maximum number of participants to load; up to 100"""
