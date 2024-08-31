from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BusinessConnectedBot
from .base import BaseMethod


@dataclass(kw_only=True)
class GetBusinessConnectedBot(BaseMethod):
    """
    Returns the business bot that is connected to the current user account. Returns a 404 error if there is no connected bot
    """

    __type__: Literal["getBusinessConnectedBot"] = "getBusinessConnectedBot"
    __returning_type__ = BusinessConnectedBot
