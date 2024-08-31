from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import AuthorizationState
from .base import BaseMethod


@dataclass(kw_only=True)
class GetAuthorizationState(BaseMethod):
    """
    Returns the current authorization state; this is an offline request. For informational purposes only. Use updateAuthorizationState instead to maintain the current authorization state. Can be called before initialization
    """

    __type__: Literal["getAuthorizationState"] = "getAuthorizationState"
    __returning_type__ = AuthorizationState
