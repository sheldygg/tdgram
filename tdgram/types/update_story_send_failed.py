from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import CanSendStoryResult, Error, Story


@dataclass(kw_only=True)
class UpdateStorySendFailed(BaseType):
    """
    A story failed to send. If the story sending is canceled, then updateStoryDeleted will be received instead of this update
    """

    __type__: Literal["updateStorySendFailed"] = "updateStorySendFailed"

    story: Story
    """The failed to send story"""
    error: Error
    """The cause of the story sending failure"""
    error_type: CanSendStoryResult | None = None
    """Type of the error; may be null if unknown"""
