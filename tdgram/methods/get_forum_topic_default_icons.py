from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Stickers
from .base import BaseMethod


@dataclass(kw_only=True)
class GetForumTopicDefaultIcons(BaseMethod):
    """
    Returns the list of custom emoji, which can be used as forum topic icon by all users
    """

    __type__: Literal["getForumTopicDefaultIcons"] = "getForumTopicDefaultIcons"
    __returning_type__ = Stickers
