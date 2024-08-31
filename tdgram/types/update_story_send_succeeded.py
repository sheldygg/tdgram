from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Story


@dataclass(kw_only=True)
class UpdateStorySendSucceeded(BaseType):
    """
    A story has been successfully sent
    """

    __type__: Literal["updateStorySendSucceeded"] = "updateStorySendSucceeded"

    story: Story
    """The sent story"""
    old_story_id: int
    """The previous temporary story identifier"""
