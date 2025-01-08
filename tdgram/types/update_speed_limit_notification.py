from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateSpeedLimitNotification(BaseType):
    """
    Download or upload file speed for the user was limited, but it can be restored by subscription to Telegram Premium. The notification can be postponed until a being downloaded or uploaded file is visible to the user.
    """

    __type__: Literal["updateSpeedLimitNotification"] = "updateSpeedLimitNotification"

    is_upload: bool
    """True, if upload speed was limited; false, if download speed was limited"""
