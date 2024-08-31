from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StatisticalGraphData(BaseType):
    """
    A graph data
    """

    __type__: Literal["statisticalGraphData"] = "statisticalGraphData"

    json_data: str
    """Graph data in JSON format"""
    zoom_token: str | None = None
    """If non-empty, a token which can be used to receive a zoomed in graph"""
