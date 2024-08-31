from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import (
        ChatStatisticsAdministratorActionsInfo,
        ChatStatisticsInviterInfo,
        ChatStatisticsMessageSenderInfo,
        DateRange,
        StatisticalGraph,
        StatisticalValue,
    )


@dataclass(kw_only=True)
class ChatStatisticsSupergroup(BaseType):
    """
    A detailed statistics about a supergroup chat
    """

    __type__: Literal["chatStatisticsSupergroup"] = "chatStatisticsSupergroup"

    period: DateRange
    """A period to which the statistics applies"""
    member_count: StatisticalValue
    """Number of members in the chat"""
    message_count: StatisticalValue
    """Number of messages sent to the chat"""
    viewer_count: StatisticalValue
    """Number of users who viewed messages in the chat"""
    sender_count: StatisticalValue
    """Number of users who sent messages to the chat"""
    member_count_graph: StatisticalGraph
    """A graph containing number of members in the chat"""
    join_graph: StatisticalGraph
    """A graph containing number of members joined and left the chat"""
    join_by_source_graph: StatisticalGraph
    """A graph containing number of new member joins per source"""
    language_graph: StatisticalGraph
    """A graph containing distribution of active users per language"""
    message_content_graph: StatisticalGraph
    """A graph containing distribution of sent messages by content type"""
    action_graph: StatisticalGraph
    """A graph containing number of different actions in the chat"""
    day_graph: StatisticalGraph
    """A graph containing distribution of message views per hour"""
    week_graph: StatisticalGraph
    """A graph containing distribution of message views per day of week"""
    top_senders: list[ChatStatisticsMessageSenderInfo]
    """List of users sent most messages in the last week"""
    top_administrators: list[ChatStatisticsAdministratorActionsInfo]
    """List of most active administrators in the last week"""
    top_inviters: list[ChatStatisticsInviterInfo]
    """List of most active inviters of new members in the last week"""
