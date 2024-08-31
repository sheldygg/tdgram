from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AuthorizationStateReady(BaseType):
    """
    The user has been successfully authorized. TDLib is now ready to answer general requests
    """

    __type__: Literal["authorizationStateReady"] = "authorizationStateReady"
