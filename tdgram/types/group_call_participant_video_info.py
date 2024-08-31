from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import GroupCallVideoSourceGroup


@dataclass(kw_only=True)
class GroupCallParticipantVideoInfo(BaseType):
    """
    Contains information about a group call participant's video channel
    """

    __type__: Literal["groupCallParticipantVideoInfo"] = "groupCallParticipantVideoInfo"

    source_groups: list[GroupCallVideoSourceGroup]
    """List of synchronization source groups of the video"""
    endpoint_id: str
    """Video channel endpoint identifier"""
    is_paused: bool
    """True, if the video is paused. This flag needs to be ignored, if new video frames are received"""
