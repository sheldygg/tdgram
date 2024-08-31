from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserTypeUnknown(BaseType):
    """
    No information on the user besides the user identifier is available, yet this user has not been deleted. This object is extremely rare and must be handled like a deleted user. It is not possible to perform any actions on users of this type
    """

    __type__: Literal["userTypeUnknown"] = "userTypeUnknown"
