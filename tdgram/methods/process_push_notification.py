from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ProcessPushNotification(BaseMethod):
    """
    Handles a push notification. Returns error with code 406 if the push notification is not supported and connection to the server is required to fetch new data. Can be called before authorization
    """

    __type__: Literal["processPushNotification"] = "processPushNotification"
    __returning_type__ = Ok

    payload: str
    """JSON-encoded push notification payload with all fields sent by the server, and 'google.sent_time' and 'google.notification.sound' fields added"""
