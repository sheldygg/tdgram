from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import AddedReactions, ReactionType
from .base import BaseMethod


@dataclass(kw_only=True)
class GetMessageAddedReactions(BaseMethod):
    """
    Returns reactions added for a message, along with their sender
    """

    __type__: Literal["getMessageAddedReactions"] = "getMessageAddedReactions"
    __returning_type__ = AddedReactions

    chat_id: int
    """Identifier of the chat to which the message belongs"""
    message_id: int
    """Identifier of the message. Use message.interaction_info.reactions.can_get_added_reactions to check whether added reactions can be received for the message"""
    reaction_type: ReactionType | None = None
    """Type of the reactions to return; pass null to return all added reactions; reactionTypePaid isn't supported"""
    offset: str
    """Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results"""
    limit: int
    """The maximum number of reactions to be returned; must be positive and can't be greater than 100"""
