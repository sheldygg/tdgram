from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeUserPhoneNumber(BaseType):
    """
    The link is a link to a user by its phone number. Call searchUserByPhoneNumber with the given phone number to process the link.
    """

    __type__: Literal["internalLinkTypeUserPhoneNumber"] = "internalLinkTypeUserPhoneNumber"

    phone_number: str
    """Phone number of the user"""
    draft_text: str
    """Draft text for message to send in the chat"""
    open_profile: bool
    """True, if user's profile information screen must be opened; otherwise, the chat itself must be opened"""
