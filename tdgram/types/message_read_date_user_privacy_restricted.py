from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageReadDateUserPrivacyRestricted(BaseType):
    """
    The read date is unknown due to privacy settings of the other user
    """

    __type__: Literal["messageReadDateUserPrivacyRestricted"] = (
        "messageReadDateUserPrivacyRestricted"
    )
