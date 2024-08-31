from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RemoveContacts(BaseMethod):
    """
    Removes users from the contact list
    """

    __type__: Literal["removeContacts"] = "removeContacts"
    __returning_type__ = Ok

    user_ids: list[int]
    """Identifiers of users to be deleted"""
