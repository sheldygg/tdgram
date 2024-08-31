from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatMembers, SupergroupMembersFilter
from .base import BaseMethod


@dataclass(kw_only=True)
class GetSupergroupMembers(BaseMethod):
    """
    Returns information about members or banned users in a supergroup or channel. Can be used only if supergroupFullInfo.can_get_members == true; additionally, administrator privileges may be required for some filters
    """

    __type__: Literal["getSupergroupMembers"] = "getSupergroupMembers"
    __returning_type__ = ChatMembers

    supergroup_id: int
    """Identifier of the supergroup or channel"""
    filter: SupergroupMembersFilter | None = None
    """The type of users to return; pass null to use supergroupMembersFilterRecent"""
    offset: int
    """Number of users to skip"""
    limit: int
    """The maximum number of users to be returned; up to 200"""
