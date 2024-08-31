from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ImportedContacts(BaseType):
    """
    Represents the result of an importContacts request
    """

    __type__: Literal["importedContacts"] = "importedContacts"

    user_ids: list[int]
    """User identifiers of the imported contacts in the same order as they were specified in the request; 0 if the contact is not yet a registered user"""
    importer_count: list[int]
    """The number of users that imported the corresponding contact; 0 for already registered users or if unavailable"""
