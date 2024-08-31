from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ConnectedWebsite


@dataclass(kw_only=True)
class ConnectedWebsites(BaseType):
    """
    Contains a list of websites the current user is logged in with Telegram
    """

    __type__: Literal["connectedWebsites"] = "connectedWebsites"

    websites: list[ConnectedWebsite]
    """List of connected websites"""
