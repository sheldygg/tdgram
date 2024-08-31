from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageSourceSearch(BaseType):
    """
    The message is from search results, including file downloads, local file list, outgoing document messages, calendar
    """

    __type__: Literal["messageSourceSearch"] = "messageSourceSearch"
