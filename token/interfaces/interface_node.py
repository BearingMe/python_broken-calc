from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Self

@dataclass
class AbstractNode(ABC):
    value: Self
    left: Self = None
    right: Self = None

    @abstractmethod
    def __eq__(self, other: Self) -> bool:
        pass