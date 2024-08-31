from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RegisterUser(BaseMethod):
    """
    Finishes user registration. Works only when the current authorization state is authorizationStateWaitRegistration
    """

    __type__: Literal["registerUser"] = "registerUser"
    __returning_type__ = Ok

    first_name: str
    """The first name of the user; 1-64 characters"""
    last_name: str
    """The last name of the user; 0-64 characters"""
    disable_notification: bool
    """Pass true to disable notification about the current user joining Telegram for other users that added them to contact list"""
