from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BusinessConnection


@dataclass(kw_only=True)
class UpdateBusinessConnection(BaseType):
    """
    A business connection has changed; for bots only
    """

    __type__: Literal["updateBusinessConnection"] = "updateBusinessConnection"

    connection: BusinessConnection
    """New data about the connection"""
