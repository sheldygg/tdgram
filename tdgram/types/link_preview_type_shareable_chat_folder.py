from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class LinkPreviewTypeShareableChatFolder(BaseType):
    """
    The link is a link to a shareable chat folder
    """

    __type__: Literal["linkPreviewTypeShareableChatFolder"] = "linkPreviewTypeShareableChatFolder"
