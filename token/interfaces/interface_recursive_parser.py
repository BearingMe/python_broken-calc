from abc import ABC, abstractmethod
from dataclasses import dataclass

from .interface_node import AbstractNode

@dataclass
class AbstractRecursiveParser(ABC):
    @abstractmethod
    def parse_factor(self, token: list) -> AbstractNode:
        pass

    @abstractmethod
    def parse_term(self, token: list) -> AbstractNode:
        pass
    
    @abstractmethod
    def parse_expression(self, token: list) -> AbstractNode:
        pass