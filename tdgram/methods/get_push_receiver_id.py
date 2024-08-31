from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import PushReceiverId
from .base import BaseMethod


@dataclass(kw_only=True)
class GetPushReceiverId(BaseMethod):
    """
    Returns a globally unique push notification subscription identifier for identification of an account, which has received a push notification. Can be called synchronously
    """

    __type__: Literal["getPushReceiverId"] = "getPushReceiverId"
    __returning_type__ = PushReceiverId

    payload: str
    """JSON-encoded push notification payload"""
