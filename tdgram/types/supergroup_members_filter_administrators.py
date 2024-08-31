from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SupergroupMembersFilterAdministrators(BaseType):
    """
    Returns the owner and administrators
    """

    __type__: Literal["supergroupMembersFilterAdministrators"] = (
        "supergroupMembersFilterAdministrators"
    )
