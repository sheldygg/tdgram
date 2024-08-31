from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import AuthorizationState


@dataclass(kw_only=True)
class UpdateAuthorizationState(BaseType):
    """
    The user authorization state has changed
    """

    __type__: Literal["updateAuthorizationState"] = "updateAuthorizationState"

    authorization_state: AuthorizationState
    """New authorization state"""
