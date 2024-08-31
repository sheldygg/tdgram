from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AuthorizationStateWaitTdlibParameters(BaseType):
    """
    Initialization parameters are needed. Call setTdlibParameters to provide them
    """

    __type__: Literal["authorizationStateWaitTdlibParameters"] = (
        "authorizationStateWaitTdlibParameters"
    )
