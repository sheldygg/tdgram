from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeBuyStars(BaseType):
    """
    The link is a link to the Telegram Star purchase section of the application
    """

    __type__: Literal["internalLinkTypeBuyStars"] = "internalLinkTypeBuyStars"

    star_count: int
    """The number of Telegram Stars that must be owned by the user"""
    purpose: str
    """Purpose of Telegram Star purchase. Arbitrary string specified by the server, for example, 'subs' if the Telegram Stars are required to extend channel subscriptions"""
