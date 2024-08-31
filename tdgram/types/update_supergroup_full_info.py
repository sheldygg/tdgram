from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import SupergroupFullInfo


@dataclass(kw_only=True)
class UpdateSupergroupFullInfo(BaseType):
    """
    Some data in supergroupFullInfo has been changed
    """

    __type__: Literal["updateSupergroupFullInfo"] = "updateSupergroupFullInfo"

    supergroup_id: int
    """Identifier of the supergroup or channel"""
    supergroup_full_info: SupergroupFullInfo
    """New full information about the supergroup"""
