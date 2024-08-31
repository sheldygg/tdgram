from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import StatisticalGraph
from .base import BaseMethod


@dataclass(kw_only=True)
class GetStatisticalGraph(BaseMethod):
    """
    Loads an asynchronous or a zoomed in statistical graph
    """

    __type__: Literal["getStatisticalGraph"] = "getStatisticalGraph"
    __returning_type__ = StatisticalGraph

    chat_id: int
    """Chat identifier"""
    token: str
    """The token for graph loading"""
    x: int
    """X-value for zoomed in graph or 0 otherwise"""
