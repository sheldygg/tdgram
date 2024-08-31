from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BasicGroupFullInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class GetBasicGroupFullInfo(BaseMethod):
    """
    Returns full information about a basic group by its identifier
    """

    __type__: Literal["getBasicGroupFullInfo"] = "getBasicGroupFullInfo"
    __returning_type__ = BasicGroupFullInfo

    basic_group_id: int
    """Basic group identifier"""
