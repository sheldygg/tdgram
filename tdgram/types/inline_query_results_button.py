from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InlineQueryResultsButtonType


@dataclass(kw_only=True)
class InlineQueryResultsButton(BaseType):
    """
    Represents a button to be shown above inline query results
    """

    __type__: Literal["inlineQueryResultsButton"] = "inlineQueryResultsButton"

    text: str
    """The text of the button"""
    type: InlineQueryResultsButtonType
    """Type of the button"""
