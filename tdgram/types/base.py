from abc import abstractmethod, ABC

from adaptix import Retort, name_mapping


retort = Retort(
    recipe=[
        name_mapping(
            map={"__type__": "@type"},
        )
    ]
)


class BaseType(ABC):
    """Base class for all types"""

    @property
    @abstractmethod
    def __type__(self) -> str:
        pass

    def dump(self):
        return retort.dump(self)