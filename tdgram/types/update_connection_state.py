from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ConnectionState


@dataclass(kw_only=True)
class UpdateConnectionState(BaseType):
    """
    The connection state has changed. This update must be used only to show a human-readable description of the connection state
    """

    __type__: Literal["updateConnectionState"] = "updateConnectionState"

    state: ConnectionState
    """The new connection state"""
