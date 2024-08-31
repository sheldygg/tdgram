from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserTypeDeleted(BaseType):
    """
    A deleted user or deleted bot. No information on the user besides the user identifier is available. It is not possible to perform any active actions on this type of user
    """

    __type__: Literal["userTypeDeleted"] = "userTypeDeleted"
