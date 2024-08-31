from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SupergroupMembersFilterBots(BaseType):
    """
    Returns bot members of the supergroup or channel
    """

    __type__: Literal["supergroupMembersFilterBots"] = "supergroupMembersFilterBots"
