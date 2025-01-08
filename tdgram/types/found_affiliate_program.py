from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import AffiliateProgramInfo


@dataclass(kw_only=True)
class FoundAffiliateProgram(BaseType):
    """
    Describes a found affiliate program
    """

    __type__: Literal["foundAffiliateProgram"] = "foundAffiliateProgram"

    bot_user_id: int
    """User identifier of the bot created the program"""
    info: AffiliateProgramInfo
    """Information about the affiliate program"""
