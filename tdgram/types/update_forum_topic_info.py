from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ForumTopicInfo


@dataclass(kw_only=True)
class UpdateForumTopicInfo(BaseType):
    """
    Basic information about a topic in a forum chat was changed
    """

    __type__: Literal["updateForumTopicInfo"] = "updateForumTopicInfo"

    chat_id: int
    """Chat identifier"""
    info: ForumTopicInfo
    """New information about the topic"""
