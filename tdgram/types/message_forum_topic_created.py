from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ForumTopicIcon


@dataclass(kw_only=True)
class MessageForumTopicCreated(BaseType):
    """
    A forum topic has been created
    """

    __type__: Literal["messageForumTopicCreated"] = "messageForumTopicCreated"

    name: str
    """Name of the topic"""
    icon: ForumTopicIcon
    """Icon of the topic"""
