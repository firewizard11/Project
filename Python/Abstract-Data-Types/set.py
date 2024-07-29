from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from referential_array import ArrayR
T = TypeVar('T')

class Set(ABC, Generic[T]):

    def __init__(self) -> None:
        self.clear()

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """Check if the set is empty"""
        pass

    @abstractmethod
    def clear(self) -> None:
        """Clear the set"""
        pass

    @abstractmethod
    def __contains__(self, item: T) -> bool:
        """Check if the set contains item"""
        pass

    @abstractmethod
    def add(self, item: T) -> None:
        """Adds item to the set"""
        pass

    @abstractmethod
    def remove(self, item: T) -> None:
        """removes item from the set"""
        pass

    @abstractmethod
    def union(self, other: Set[T]) -> Set[T]:
        pass

    @abstractmethod
    def intersection(self, other: Set[T]) -> Set[T]:
        pass

    @abstractmethod
    def difference(self, other: Set[T]) -> Set[T]:
        pass


class ArraySet(Set[T]):
    MIN_CAPACITY = 1

    def __init__(self, capacity: int = 1) -> None:
        Set.__init__(self)
        self.array = ArrayR(max(self.MIN_CAPACITY, capacity))

    def clear(self) -> None:
        self.size = 0

    def __len__(self) -> int:
        return self.size
    
    def is_empty(self) -> bool:
        return len(self) == 0
    
    def is_full(self):
        return len(self) == len(self.array)
    
    def __contains__(self, item: T) -> bool:
        for i in range(self.size):
            if item == self.array[i]:
                return True
        return False
    
    def add(self, item: T) -> None:
        if item not in self:
            if self.is_full():
                raise Exception("Set is full")
            
            self.array[self.size] = item
            self.size += 1

    def remove(self, item: T) -> None:
        for i in range(self.size):
            if item == self.array[i]:
                self.array[i] = self.array[self.size - 1]
                self.size -= 1
                break
        else:
            raise KeyError(item)
        
    def union(self, other: ArraySet[T]) -> ArraySet[T]:
        res = ArraySet(len(self.array) + len(other.array))
        
        for i in range(len(self)):
            res.array[i] = self.array[i]
        res.size = self.size
        
        for j in range(len(other)):
            res.add(other.array[j])

        return res