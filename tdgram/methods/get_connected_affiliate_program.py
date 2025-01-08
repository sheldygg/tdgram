from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import AffiliateType, ConnectedAffiliateProgram
from .base import BaseMethod


@dataclass(kw_only=True)
class GetConnectedAffiliateProgram(BaseMethod):
    """
    Returns an affiliate program that were connected to the given affiliate by identifier of the bot that created the program
    """

    __type__: Literal["getConnectedAffiliateProgram"] = "getConnectedAffiliateProgram"
    __returning_type__ = ConnectedAffiliateProgram

    affiliate: AffiliateType
    """The affiliate to which the affiliate program will be connected"""
    bot_user_id: int
    """Identifier of the bot that created the program"""
