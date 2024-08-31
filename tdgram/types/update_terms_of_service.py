from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import TermsOfService


@dataclass(kw_only=True)
class UpdateTermsOfService(BaseType):
    """
    New terms of service must be accepted by the user. If the terms of service are declined, then the deleteAccount method must be called with the reason 'Decline ToS update'
    """

    __type__: Literal["updateTermsOfService"] = "updateTermsOfService"

    terms_of_service_id: str
    """Identifier of the terms of service"""
    terms_of_service: TermsOfService
    """The new terms of service"""
