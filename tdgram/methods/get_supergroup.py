from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Supergroup
from .base import BaseMethod


@dataclass(kw_only=True)
class GetSupergroup(BaseMethod):
    """
    Returns information about a supergroup or a channel by its identifier. This is an offline request if the current user is not a bot
    """

    __type__: Literal["getSupergroup"] = "getSupergroup"
    __returning_type__ = Supergroup

    supergroup_id: int
    """Supergroup or channel identifier"""
