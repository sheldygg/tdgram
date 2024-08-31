from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class EnableProxy(BaseMethod):
    """
    Enables a proxy. Only one proxy can be enabled at a time. Can be called before authorization
    """

    __type__: Literal["enableProxy"] = "enableProxy"
    __returning_type__ = Ok

    proxy_id: int
    """Proxy identifier"""
