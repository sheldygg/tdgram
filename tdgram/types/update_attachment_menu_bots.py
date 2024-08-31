from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import AttachmentMenuBot


@dataclass(kw_only=True)
class UpdateAttachmentMenuBots(BaseType):
    """
    The list of bots added to attachment or side menu has changed
    """

    __type__: Literal["updateAttachmentMenuBots"] = "updateAttachmentMenuBots"

    bots: list[AttachmentMenuBot]
    """The new list of bots. The bots must not be shown on scheduled messages screen"""
