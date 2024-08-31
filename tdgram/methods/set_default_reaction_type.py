from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, ReactionType
from .base import BaseMethod


@dataclass(kw_only=True)
class SetDefaultReactionType(BaseMethod):
    """
    Changes type of default reaction for the current user
    """

    __type__: Literal["setDefaultReactionType"] = "setDefaultReactionType"
    __returning_type__ = Ok

    reaction_type: ReactionType
    """New type of the default reaction. The paid reaction can't be set as default"""
