from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Proxies
from .base import BaseMethod


@dataclass(kw_only=True)
class GetProxies(BaseMethod):
    """
    Returns the list of proxies that are currently set up. Can be called before authorization
    """

    __type__: Literal["getProxies"] = "getProxies"
    __returning_type__ = Proxies
