from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StatisticalGraph


@dataclass(kw_only=True)
class StoryStatistics(BaseType):
    """
    A detailed statistics about a story
    """

    __type__: Literal["storyStatistics"] = "storyStatistics"

    story_interaction_graph: StatisticalGraph
    """A graph containing number of story views and shares"""
    story_reaction_graph: StatisticalGraph
    """A graph containing number of story reactions"""
