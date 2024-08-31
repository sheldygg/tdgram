from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatStatisticsInteractionInfo, DateRange, StatisticalGraph, StatisticalValue


@dataclass(kw_only=True)
class ChatStatisticsChannel(BaseType):
    """
    A detailed statistics about a channel chat
    """

    __type__: Literal["chatStatisticsChannel"] = "chatStatisticsChannel"

    period: DateRange
    """A period to which the statistics applies"""
    member_count: StatisticalValue
    """Number of members in the chat"""
    mean_message_view_count: StatisticalValue
    """Mean number of times the recently sent messages were viewed"""
    mean_message_share_count: StatisticalValue
    """Mean number of times the recently sent messages were shared"""
    mean_message_reaction_count: StatisticalValue
    """Mean number of times reactions were added to the recently sent messages"""
    mean_story_view_count: StatisticalValue
    """Mean number of times the recently sent stories were viewed"""
    mean_story_share_count: StatisticalValue
    """Mean number of times the recently sent stories were shared"""
    mean_story_reaction_count: StatisticalValue
    """Mean number of times reactions were added to the recently sent stories"""
    enabled_notifications_percentage: float
    """A percentage of users with enabled notifications for the chat; 0-100"""
    member_count_graph: StatisticalGraph
    """A graph containing number of members in the chat"""
    join_graph: StatisticalGraph
    """A graph containing number of members joined and left the chat"""
    mute_graph: StatisticalGraph
    """A graph containing number of members muted and unmuted the chat"""
    view_count_by_hour_graph: StatisticalGraph
    """A graph containing number of message views in a given hour in the last two weeks"""
    view_count_by_source_graph: StatisticalGraph
    """A graph containing number of message views per source"""
    join_by_source_graph: StatisticalGraph
    """A graph containing number of new member joins per source"""
    language_graph: StatisticalGraph
    """A graph containing number of users viewed chat messages per language"""
    message_interaction_graph: StatisticalGraph
    """A graph containing number of chat message views and shares"""
    message_reaction_graph: StatisticalGraph
    """A graph containing number of reactions on messages"""
    story_interaction_graph: StatisticalGraph
    """A graph containing number of story views and shares"""
    story_reaction_graph: StatisticalGraph
    """A graph containing number of reactions on stories"""
    instant_view_interaction_graph: StatisticalGraph
    """A graph containing number of views of associated with the chat instant views"""
    recent_interactions: list[ChatStatisticsInteractionInfo]
    """Detailed statistics about number of views and shares of recently sent messages and stories"""
