from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FileTypeNotificationSound(BaseType):
    """
    The file is a notification sound
    """

    __type__: Literal["fileTypeNotificationSound"] = "fileTypeNotificationSound"
