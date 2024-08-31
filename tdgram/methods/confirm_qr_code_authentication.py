from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Session
from .base import BaseMethod


@dataclass(kw_only=True)
class ConfirmQrCodeAuthentication(BaseMethod):
    """
    Confirms QR code authentication on another device. Returns created session on success
    """

    __type__: Literal["confirmQrCodeAuthentication"] = "confirmQrCodeAuthentication"
    __returning_type__ = Session

    link: str
    """A link from a QR code. The link must be scanned by the in-app camera"""
