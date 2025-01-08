from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Gift


@dataclass(kw_only=True)
class MessageRefundedUpgradedGift(BaseType):
    """
    A gift which purchase, upgrade or transfer were refunded
    """

    __type__: Literal["messageRefundedUpgradedGift"] = "messageRefundedUpgradedGift"

    gift: Gift
    """The gift"""
    is_upgrade: bool
    """True, if the gift was obtained by upgrading of a previously received gift"""
