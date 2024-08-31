from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import SupergroupFullInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class GetSupergroupFullInfo(BaseMethod):
    """
    Returns full information about a supergroup or a channel by its identifier, cached for up to 1 minute
    """

    __type__: Literal["getSupergroupFullInfo"] = "getSupergroupFullInfo"
    __returning_type__ = SupergroupFullInfo

    supergroup_id: int
    """Supergroup or channel identifier"""
