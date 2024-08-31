from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageSender


@dataclass(kw_only=True)
class MessageProximityAlertTriggered(BaseType):
    """
    A user in the chat came within proximity alert range
    """

    __type__: Literal["messageProximityAlertTriggered"] = "messageProximityAlertTriggered"

    traveler_id: MessageSender
    """The identifier of a user or chat that triggered the proximity alert"""
    watcher_id: MessageSender
    """The identifier of a user or chat that subscribed for the proximity alert"""
    distance: int
    """The distance between the users"""
