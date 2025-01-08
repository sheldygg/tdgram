from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import UserGift
from .base import BaseMethod


@dataclass(kw_only=True)
class GetUserGift(BaseMethod):
    """
    Returns information about a gift received or sent by the current user
    """

    __type__: Literal["getUserGift"] = "getUserGift"
    __returning_type__ = UserGift

    message_id: int
    """Identifier of the message with the gift"""
