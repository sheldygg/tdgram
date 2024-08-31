from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateNewCustomQuery(BaseType):
    """
    A new incoming query; for bots only
    """

    __type__: Literal["updateNewCustomQuery"] = "updateNewCustomQuery"

    id: int
    """The query identifier"""
    data: str
    """JSON-serialized query data"""
    timeout: int
    """Query timeout"""
