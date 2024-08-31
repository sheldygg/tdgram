from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ReplyMarkup


@dataclass(kw_only=True)
class InputInlineQueryResultGame(BaseType):
    """
    Represents a game
    """

    __type__: Literal["inputInlineQueryResultGame"] = "inputInlineQueryResultGame"

    id: str
    """Unique identifier of the query result"""
    game_short_name: str
    """Short name of the game"""
    reply_markup: ReplyMarkup | None = None
    """The message reply markup; pass null if none. Must be of type replyMarkupInlineKeyboard or null"""
