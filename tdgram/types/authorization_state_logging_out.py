from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AuthorizationStateLoggingOut(BaseType):
    """
    The user is currently logging out
    """

    __type__: Literal["authorizationStateLoggingOut"] = "authorizationStateLoggingOut"
