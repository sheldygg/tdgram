from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import HttpUrl
from .base import BaseMethod


@dataclass(kw_only=True)
class GetGroupCallInviteLink(BaseMethod):
    """
    Returns invite link to a video chat in a public chat
    """

    __type__: Literal["getGroupCallInviteLink"] = "getGroupCallInviteLink"
    __returning_type__ = HttpUrl

    group_call_id: int
    """Group call identifier"""
    can_self_unmute: bool
    """Pass true if the invite link needs to contain an invite hash, passing which to joinGroupCall would allow the invited user to unmute themselves. Requires groupCall.can_be_managed group call flag"""
