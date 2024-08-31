from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeChatFolderSettings(BaseType):
    """
    The link is a link to the folder section of the application settings
    """

    __type__: Literal["internalLinkTypeChatFolderSettings"] = "internalLinkTypeChatFolderSettings"
