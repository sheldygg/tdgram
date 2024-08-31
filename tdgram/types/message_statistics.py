from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StatisticalGraph


@dataclass(kw_only=True)
class MessageStatistics(BaseType):
    """
    A detailed statistics about a message
    """

    __type__: Literal["messageStatistics"] = "messageStatistics"

    message_interaction_graph: StatisticalGraph
    """A graph containing number of message views and shares"""
    message_reaction_graph: StatisticalGraph
    """A graph containing number of message reactions"""
