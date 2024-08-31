from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StatisticalGraphAsync(BaseType):
    """
    The graph data to be asynchronously loaded through getStatisticalGraph
    """

    __type__: Literal["statisticalGraphAsync"] = "statisticalGraphAsync"

    token: str
    """The token to use for data loading"""
