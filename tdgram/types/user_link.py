from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserLink(BaseType):
    """
    Contains an HTTPS URL, which can be used to get information about a user
    """

    __type__: Literal["userLink"] = "userLink"

    url: str
    """The URL"""
    expires_in: int
    """Left time for which the link is valid, in seconds; 0 if the link is a public username link"""
