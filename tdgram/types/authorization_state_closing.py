from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AuthorizationStateClosing(BaseType):
    """
    TDLib is closing, all subsequent queries will be answered with the error 500. Note that closing TDLib can take a while. All resources will be freed only after authorizationStateClosed has been received
    """

    __type__: Literal["authorizationStateClosing"] = "authorizationStateClosing"
