from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import AffiliateType, ConnectedAffiliateProgram
from .base import BaseMethod


@dataclass(kw_only=True)
class ConnectAffiliateProgram(BaseMethod):
    """
    Connects an affiliate program to the given affiliate. Returns information about the connected affiliate program
    """

    __type__: Literal["connectAffiliateProgram"] = "connectAffiliateProgram"
    __returning_type__ = ConnectedAffiliateProgram

    affiliate: AffiliateType
    """The affiliate to which the affiliate program will be connected"""
    bot_user_id: int
    """Identifier of the bot, which affiliate program is connected"""
