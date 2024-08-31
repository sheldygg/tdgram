from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class Contact(BaseType):
    """
    Describes a user contact
    """

    __type__: Literal["contact"] = "contact"

    phone_number: str
    """Phone number of the user"""
    first_name: str
    """First name of the user; 1-255 characters in length"""
    last_name: str
    """Last name of the user"""
    vcard: str
    """Additional data about the user in a form of vCard; 0-2048 bytes in length"""
    user_id: int
    """Identifier of the user, if known; 0 otherwise"""
