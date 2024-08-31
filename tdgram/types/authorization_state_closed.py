from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AuthorizationStateClosed(BaseType):
    """
    TDLib client is in its final state. All databases are closed and all resources are released. No other updates will be received after this. All queries will be responded to
    """

    __type__: Literal["authorizationStateClosed"] = "authorizationStateClosed"
