from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import LogTags
from .base import BaseMethod


@dataclass(kw_only=True)
class GetLogTags(BaseMethod):
    """
    Returns the list of available TDLib internal log tags, for example, ['actor', 'binlog', 'connections', 'notifications', 'proxy']. Can be called synchronously
    """

    __type__: Literal["getLogTags"] = "getLogTags"
    __returning_type__ = LogTags
