from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BotWriteAccessAllowReasonConnectedWebsite(BaseType):
    """
    The user connected a website by logging in using Telegram Login Widget on it
    """

    __type__: Literal["botWriteAccessAllowReasonConnectedWebsite"] = (
        "botWriteAccessAllowReasonConnectedWebsite"
    )

    domain_name: str
    """Domain name of the connected website"""
