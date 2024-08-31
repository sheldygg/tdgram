from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BasicGroup


@dataclass(kw_only=True)
class UpdateBasicGroup(BaseType):
    """
    Some data of a basic group has changed. This update is guaranteed to come before the basic group identifier is returned to the application
    """

    __type__: Literal["updateBasicGroup"] = "updateBasicGroup"

    basic_group: BasicGroup
    """New data about the group"""
