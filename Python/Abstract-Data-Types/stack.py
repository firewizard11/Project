from typing import TypeVar, Generic
T = TypeVar('T')

class Stack(Generic[T]):

    def __init__(self) -> None:
        self.length = 0

    def push(self, item: T) -> None:
        pass

    def pop(self) -> T:
        pass

    def peek(self) -> T:
        pass

    def __len__(self) -> int:
        return self.length
    
    def is_empty(self) -> bool:
        return len(self) == 0
    
    def is_full(self) -> bool:
        pass

    def clear(self) -> None:
        self.length = 0