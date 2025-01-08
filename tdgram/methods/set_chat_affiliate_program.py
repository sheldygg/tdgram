from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import AffiliateProgramParameters, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetChatAffiliateProgram(BaseMethod):
    """
    Changes affiliate program for a bot
    """

    __type__: Literal["setChatAffiliateProgram"] = "setChatAffiliateProgram"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat with an owned bot for which affiliate program is changed"""
    parameters: AffiliateProgramParameters | None = None
    """Parameters of the affiliate program; pass null to close the currently active program. If there is an active program, then commission and program duration can only be increased."""
