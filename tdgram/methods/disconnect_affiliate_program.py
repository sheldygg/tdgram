from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import AffiliateType, ConnectedAffiliateProgram
from .base import BaseMethod


@dataclass(kw_only=True)
class DisconnectAffiliateProgram(BaseMethod):
    """
    Disconnects an affiliate program from the given affiliate and immediately deactivates its referral link. Returns updated information about the disconnected affiliate program
    """

    __type__: Literal["disconnectAffiliateProgram"] = "disconnectAffiliateProgram"
    __returning_type__ = ConnectedAffiliateProgram

    affiliate: AffiliateType
    """The affiliate to which the affiliate program is connected"""
    url: str
    """The referral link of the affiliate program"""
