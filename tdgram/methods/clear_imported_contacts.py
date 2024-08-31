from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ClearImportedContacts(BaseMethod):
    """
    Clears all imported contacts, contact list remains unchanged
    """

    __type__: Literal["clearImportedContacts"] = "clearImportedContacts"
    __returning_type__ = Ok
