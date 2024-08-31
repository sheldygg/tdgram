from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class KeyboardButtonTypeRequestUsers(BaseType):
    """
    A button that requests users to be shared by the current user; available only in private chats. Use the method shareUsersWithBot to complete the request
    """

    __type__: Literal["keyboardButtonTypeRequestUsers"] = "keyboardButtonTypeRequestUsers"

    id: int
    """Unique button identifier"""
    restrict_user_is_bot: bool
    """True, if the shared users must or must not be bots"""
    user_is_bot: bool
    """True, if the shared users must be bots; otherwise, the shared users must not be bots. Ignored if restrict_user_is_bot is false"""
    restrict_user_is_premium: bool
    """True, if the shared users must or must not be Telegram Premium users"""
    user_is_premium: bool
    """True, if the shared users must be Telegram Premium users; otherwise, the shared users must not be Telegram Premium users. Ignored if restrict_user_is_premium is false"""
    max_quantity: int
    """The maximum number of users to share"""
    request_name: bool
    """Pass true to request name of the users; bots only"""
    request_username: bool
    """Pass true to request username of the users; bots only"""
    request_photo: bool
    """Pass true to request photo of the users; bots only"""
