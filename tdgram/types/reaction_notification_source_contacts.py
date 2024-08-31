from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReactionNotificationSourceContacts(BaseType):
    """
    Notifications for reactions are shown only for reactions from contacts
    """

    __type__: Literal["reactionNotificationSourceContacts"] = "reactionNotificationSourceContacts"
