from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Seconds
from .base import BaseMethod


@dataclass(kw_only=True)
class PingProxy(BaseMethod):
    """
    Computes time needed to receive a response from a Telegram server through a proxy. Can be called before authorization
    """

    __type__: Literal["pingProxy"] = "pingProxy"
    __returning_type__ = Seconds

    proxy_id: int
    """Proxy identifier. Use 0 to ping a Telegram server without a proxy"""
