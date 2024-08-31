from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageReadDateMyPrivacyRestricted(BaseType):
    """
    The read date is unknown due to privacy settings of the current user, but will be known if the user subscribes to Telegram Premium
    """

    __type__: Literal["messageReadDateMyPrivacyRestricted"] = "messageReadDateMyPrivacyRestricted"
