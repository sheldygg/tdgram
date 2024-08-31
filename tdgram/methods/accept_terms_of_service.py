from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class AcceptTermsOfService(BaseMethod):
    """
    Accepts Telegram terms of services
    """

    __type__: Literal["acceptTermsOfService"] = "acceptTermsOfService"
    __returning_type__ = Ok

    terms_of_service_id: str
    """Terms of service identifier"""
