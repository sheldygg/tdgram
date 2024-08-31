from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatsNearby, Location
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchChatsNearby(BaseMethod):
    """
    Returns a list of users and location-based supergroups nearby. The list of users nearby will be updated for 60 seconds after the request by the updates updateUsersNearby.
    """

    __type__: Literal["searchChatsNearby"] = "searchChatsNearby"
    __returning_type__ = ChatsNearby

    location: Location
    """Current user location"""
