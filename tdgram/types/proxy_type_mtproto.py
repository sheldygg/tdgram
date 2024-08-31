from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ProxyTypeMtproto(BaseType):
    """
    An MTProto proxy server
    """

    __type__: Literal["proxyTypeMtproto"] = "proxyTypeMtproto"

    secret: str
    """The proxy's secret in hexadecimal encoding"""
