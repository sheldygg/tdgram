from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Proxy


@dataclass(kw_only=True)
class Proxies(BaseType):
    """
    Represents a list of proxy servers
    """

    __type__: Literal["proxies"] = "proxies"

    proxies: list[Proxy]
    """List of proxy servers"""
