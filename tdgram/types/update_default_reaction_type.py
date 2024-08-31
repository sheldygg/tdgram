from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ReactionType


@dataclass(kw_only=True)
class UpdateDefaultReactionType(BaseType):
    """
    The type of default reaction has changed
    """

    __type__: Literal["updateDefaultReactionType"] = "updateDefaultReactionType"

    reaction_type: ReactionType
    """The new type of the default reaction"""
