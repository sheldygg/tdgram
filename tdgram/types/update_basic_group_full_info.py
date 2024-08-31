from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BasicGroupFullInfo


@dataclass(kw_only=True)
class UpdateBasicGroupFullInfo(BaseType):
    """
    Some data in basicGroupFullInfo has been changed
    """

    __type__: Literal["updateBasicGroupFullInfo"] = "updateBasicGroupFullInfo"

    basic_group_id: int
    """Identifier of a basic group"""
    basic_group_full_info: BasicGroupFullInfo
    """New full information about the group"""
