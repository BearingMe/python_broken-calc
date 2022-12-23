from abc import ABC, abstractmethod

class AbstractSymbolizer(ABC):
    @abstractmethod
    def validate_input(self, expression: str) -> bool:
        pass

    @abstractmethod
    def create_symbol(self, expression: str) -> list:
        pass