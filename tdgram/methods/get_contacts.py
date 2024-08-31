from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Users
from .base import BaseMethod


@dataclass(kw_only=True)
class GetContacts(BaseMethod):
    """
    Returns all contacts of the user
    """

    __type__: Literal["getContacts"] = "getContacts"
    __returning_type__ = Users
