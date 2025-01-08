from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Photo


@dataclass(kw_only=True)
class StarSubscriptionTypeBot(BaseType):
    """
    Describes a subscription in a bot or a business account
    """

    __type__: Literal["starSubscriptionTypeBot"] = "starSubscriptionTypeBot"

    is_canceled_by_bot: bool
    """True, if the subscription was canceled by the bot and can't be extended"""
    title: str
    """Subscription invoice title"""
    photo: Photo
    """Subscription invoice photo"""
    invoice_link: str
    """The link to the subscription invoice"""
