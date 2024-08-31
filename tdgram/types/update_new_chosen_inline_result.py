from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Location


@dataclass(kw_only=True)
class UpdateNewChosenInlineResult(BaseType):
    """
    The user has chosen a result of an inline query; for bots only
    """

    __type__: Literal["updateNewChosenInlineResult"] = "updateNewChosenInlineResult"

    sender_user_id: int
    """Identifier of the user who sent the query"""
    user_location: Location | None = None
    """User location; may be null"""
    query: str
    """Text of the query"""
    result_id: str
    """Identifier of the chosen result"""
    inline_message_id: str
    """Identifier of the sent inline message, if known"""
