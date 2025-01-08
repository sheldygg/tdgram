from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StarSubscriptionTypeChannel(BaseType):
    """
    Describes a subscription to a channel chat
    """

    __type__: Literal["starSubscriptionTypeChannel"] = "starSubscriptionTypeChannel"

    can_reuse: bool
    """True, if the subscription is active and the user can use the method reuseStarSubscription to join the subscribed chat again"""
    invite_link: str | None = None
    """The invite link that can be used to renew the subscription if it has been expired; may be empty, if the link isn't available anymore"""
