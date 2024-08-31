from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatPermissions


@dataclass(kw_only=True)
class ChatEventPermissionsChanged(BaseType):
    """
    The chat permissions were changed
    """

    __type__: Literal["chatEventPermissionsChanged"] = "chatEventPermissionsChanged"

    old_permissions: ChatPermissions
    """Previous chat permissions"""
    new_permissions: ChatPermissions
    """New chat permissions"""
