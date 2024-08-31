from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BusinessConnection
from .base import BaseMethod


@dataclass(kw_only=True)
class GetBusinessConnection(BaseMethod):
    """
    Returns information about a business connection by its identifier; for bots only
    """

    __type__: Literal["getBusinessConnection"] = "getBusinessConnection"
    __returning_type__ = BusinessConnection

    connection_id: str
    """Identifier of the business connection to return"""
