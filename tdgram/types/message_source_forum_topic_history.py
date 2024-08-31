from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageSourceForumTopicHistory(BaseType):
    """
    The message is from a forum topic history
    """

    __type__: Literal["messageSourceForumTopicHistory"] = "messageSourceForumTopicHistory"
