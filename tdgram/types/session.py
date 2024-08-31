from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import SessionType


@dataclass(kw_only=True)
class Session(BaseType):
    """
    Contains information about one session in a Telegram application used by the current user. Sessions must be shown to the user in the returned order
    """

    __type__: Literal["session"] = "session"

    id: int
    """Session identifier"""
    is_current: bool
    """True, if this session is the current session"""
    is_password_pending: bool
    """True, if a 2-step verification password is needed to complete authorization of the session"""
    is_unconfirmed: bool
    """True, if the session wasn't confirmed from another session"""
    can_accept_secret_chats: bool
    """True, if incoming secret chats can be accepted by the session"""
    can_accept_calls: bool
    """True, if incoming calls can be accepted by the session"""
    type: SessionType
    """Session type based on the system and application version, which can be used to display a corresponding icon"""
    api_id: int
    """Telegram API identifier, as provided by the application"""
    application_name: str
    """Name of the application, as provided by the application"""
    application_version: str
    """The version of the application, as provided by the application"""
    is_official_application: bool
    """True, if the application is an official application or uses the api_id of an official application"""
    device_model: str
    """Model of the device the application has been run or is running on, as provided by the application"""
    platform: str
    """Operating system the application has been run or is running on, as provided by the application"""
    system_version: str
    """Version of the operating system the application has been run or is running on, as provided by the application"""
    log_in_date: int
    """Point in time (Unix timestamp) when the user has logged in"""
    last_active_date: int
    """Point in time (Unix timestamp) when the session was last used"""
    ip_address: str
    """IP address from which the session was created, in human-readable format"""
    location: str
    """A human-readable description of the location from which the session was created, based on the IP address"""
