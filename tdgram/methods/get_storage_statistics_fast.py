from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import StorageStatisticsFast
from .base import BaseMethod


@dataclass(kw_only=True)
class GetStorageStatisticsFast(BaseMethod):
    """
    Quickly returns approximate storage usage statistics. Can be called before authorization
    """

    __type__: Literal["getStorageStatisticsFast"] = "getStorageStatisticsFast"
    __returning_type__ = StorageStatisticsFast
