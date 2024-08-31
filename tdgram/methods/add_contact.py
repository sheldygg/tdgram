from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Contact, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class AddContact(BaseMethod):
    """
    Adds a user to the contact list or edits an existing contact by their user identifier
    """

    __type__: Literal["addContact"] = "addContact"
    __returning_type__ = Ok

    contact: Contact
    """The contact to add or edit; phone number may be empty and needs to be specified only if known, vCard is ignored"""
    share_phone_number: bool
    """Pass true to share the current user's phone number with the new contact. A corresponding rule to userPrivacySettingShowPhoneNumber will be added if needed."""
