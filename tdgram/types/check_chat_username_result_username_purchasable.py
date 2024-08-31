from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CheckChatUsernameResultUsernamePurchasable(BaseType):
    """
    The username can be purchased at https://fragment.com. Information about the username can be received using getCollectibleItemInfo
    """

    __type__: Literal["checkChatUsernameResultUsernamePurchasable"] = (
        "checkChatUsernameResultUsernamePurchasable"
    )
