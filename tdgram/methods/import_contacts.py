from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Contact, ImportedContacts
from .base import BaseMethod


@dataclass(kw_only=True)
class ImportContacts(BaseMethod):
    """
    Adds new contacts or edits existing contacts by their phone numbers; contacts' user identifiers are ignored
    """

    __type__: Literal["importContacts"] = "importContacts"
    __returning_type__ = ImportedContacts

    contacts: list[Contact]
    """The list of contacts to import or edit; contacts' vCard are ignored and are not imported"""
