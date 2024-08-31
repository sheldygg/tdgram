from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SearchMessagesFilterPhotoAndVideo(BaseType):
    """
    Returns only photo and video messages
    """

    __type__: Literal["searchMessagesFilterPhotoAndVideo"] = "searchMessagesFilterPhotoAndVideo"
