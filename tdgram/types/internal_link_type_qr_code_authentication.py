from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeQrCodeAuthentication(BaseType):
    """
    The link can be used to login the current user on another device, but it must be scanned from QR-code using in-app camera. An alert similar to
    """

    __type__: Literal["internalLinkTypeQrCodeAuthentication"] = (
        "internalLinkTypeQrCodeAuthentication"
    )
