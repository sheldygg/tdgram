from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Users
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchContacts(BaseMethod):
    """
    Searches for the specified query in the first names, last names and usernames of the known user contacts
    """

    __type__: Literal["searchContacts"] = "searchContacts"
    __returning_type__ = Users

    query: str | None = None
    """Query to search for; may be empty to return all contacts"""
    limit: int
    """The maximum number of users to be returned"""
