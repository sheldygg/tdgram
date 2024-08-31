from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Animation


@dataclass(kw_only=True)
class InlineQueryResultAnimation(BaseType):
    """
    Represents an animation file
    """

    __type__: Literal["inlineQueryResultAnimation"] = "inlineQueryResultAnimation"

    id: str
    """Unique identifier of the query result"""
    animation: Animation
    """Animation file"""
    title: str
    """Animation title"""
