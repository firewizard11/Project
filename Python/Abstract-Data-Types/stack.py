from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from referential_array import ArrayR
T = TypeVar('T')

class Stack(ABC, Generic[T]):

    def __init__(self) -> None:
        self.length = 0

    @abstractmethod
    def push(self, item: T) -> None:
        pass

    @abstractmethod
    def pop(self) -> T:
        pass

    @abstractmethod
    def peek(self) -> T:
        pass

    def __len__(self) -> int:
        return self.length
    
    def is_empty(self) -> bool:
        return len(self) == 0
    
    @abstractmethod
    def is_full(self) -> bool:
        pass

    def clear(self) -> None:
        self.length = 0


class ArrayStack(Stack[T]):
    
    MIN_CAPACITY = 1

    def __init__(self, max_capacity: int) -> None:
        Stack.__init__(self)
        self.array = ArrayR(max(self.MIN_CAPACITY, max_capacity))

    def is_full(self) -> bool:
        return len(self) == len(self.array)
    
    def push(self, item: T) -> None:
        if self.is_full():
            raise Exception("Stack is full")
        
        self.array[len(self)] = item
        self.length += 1

    def pop(self) -> T:
        if self.is_empty():
            raise Exception("Stack is empty")
        
        self.length -= 1
        return self.array[self.length]
    
    def peek(self) -> T:
        if self.is_empty():
            raise Exception("Stack is empty")
        
        return self.array[self.length-1]