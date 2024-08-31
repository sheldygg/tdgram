from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SavedMessagesTopicTypeAuthorHidden(BaseType):
    """
    Topic containing messages forwarded from a user with hidden privacy
    """

    __type__: Literal["savedMessagesTopicTypeAuthorHidden"] = "savedMessagesTopicTypeAuthorHidden"
