from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BusinessFeatureChatFolderTags(BaseType):
    """
    The ability to display folder names for each chat in the chat list
    """

    __type__: Literal["businessFeatureChatFolderTags"] = "businessFeatureChatFolderTags"
