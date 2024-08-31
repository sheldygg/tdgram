from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BasicGroup
from .base import BaseMethod


@dataclass(kw_only=True)
class GetBasicGroup(BaseMethod):
    """
    Returns information about a basic group by its identifier. This is an offline request if the current user is not a bot
    """

    __type__: Literal["getBasicGroup"] = "getBasicGroup"
    __returning_type__ = BasicGroup

    basic_group_id: int
    """Basic group identifier"""
