from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ConnectedWebsite(BaseType):
    """
    Contains information about one website the current user is logged in with Telegram
    """

    __type__: Literal["connectedWebsite"] = "connectedWebsite"

    id: int
    """Website identifier"""
    domain_name: str
    """The domain name of the website"""
    bot_user_id: int
    """User identifier of a bot linked with the website"""
    browser: str
    """The version of a browser used to log in"""
    platform: str
    """Operating system the browser is running on"""
    log_in_date: int
    """Point in time (Unix timestamp) when the user was logged in"""
    last_active_date: int
    """Point in time (Unix timestamp) when obtained authorization was last used"""
    ip_address: str
    """IP address from which the user was logged in, in human-readable format"""
    location: str
    """Human-readable description of a country and a region from which the user was logged in, based on the IP address"""
