from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Contact, ImportedContacts
from .base import BaseMethod


@dataclass(kw_only=True)
class ChangeImportedContacts(BaseMethod):
    """
    Changes imported contacts using the list of contacts saved on the device. Imports newly added contacts and, if at least the file database is enabled, deletes recently deleted contacts.
    """

    __type__: Literal["changeImportedContacts"] = "changeImportedContacts"
    __returning_type__ = ImportedContacts

    contacts: list[Contact]
    """The new list of contacts, contact's vCard are ignored and are not imported"""
