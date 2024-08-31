from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UnconfirmedSession(BaseType):
    """
    Contains information about an unconfirmed session
    """

    __type__: Literal["unconfirmedSession"] = "unconfirmedSession"

    id: int
    """Session identifier"""
    log_in_date: int
    """Point in time (Unix timestamp) when the user has logged in"""
    device_model: str
    """Model of the device that was used for the session creation, as provided by the application"""
    location: str
    """A human-readable description of the location from which the session was created, based on the IP address"""
