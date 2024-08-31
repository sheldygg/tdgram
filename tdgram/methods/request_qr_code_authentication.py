from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RequestQrCodeAuthentication(BaseMethod):
    """
    Requests QR code authentication by scanning a QR code on another logged in device. Works only when the current authorization state is authorizationStateWaitPhoneNumber,
    """

    __type__: Literal["requestQrCodeAuthentication"] = "requestQrCodeAuthentication"
    __returning_type__ = Ok

    other_user_ids: list[int]
    """List of user identifiers of other users currently using the application"""
