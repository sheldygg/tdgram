from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RemoveProxy(BaseMethod):
    """
    Removes a proxy server. Can be called before authorization
    """

    __type__: Literal["removeProxy"] = "removeProxy"
    __returning_type__ = Ok

    proxy_id: int
    """Proxy identifier"""
