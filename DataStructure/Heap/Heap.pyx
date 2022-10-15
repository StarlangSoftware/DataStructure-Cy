from typing import Callable

from DataStructure.Heap.HeapNode cimport HeapNode


cdef class Heap:

    def __init__(self, N: int, comparator: Callable[[object, object], int]):
        self.comparator = comparator
        self.__count = 0
        self.__array = []
        self.__N = N
        for i in range(N):
            self.__array.append(None)

    def compare(self, data1: object, data2: object) -> int:
        pass

    cpdef bint isEmpty(self):
        return self.__count == 0

    cpdef swapNode(self, int index1, int index2):
        cdef HeapNode tmp
        tmp = self.__array[index1]
        self.__array[index1] = self.__array[index2]
        self.__array[index2] = tmp

    cpdef percolateDown(self, int no):
        cdef int left, right
        left = 2 * no + 1
        right = 2 * no + 2
        while (left < self.__count and self.compare(self.__array[no].getData(), self.__array[left].getData()) < 0) or \
                (right < self.__count and self.compare(self.__array[no].getData(), self.__array[right].getData()) < 0):
            if right >= self.__count or self.compare(self.__array[left].getData(), self.__array[right].getData()) > 0:
                self.swapNode(no, left)
                no = left
            else:
                self.swapNode(no, right)
                no = right
            left = 2 * no + 1
            right = 2 * no + 2

    cpdef percolateUp(self, int no):
        cdef int parent
        parent = (no - 1) // 2
        while parent >= 0 and self.compare(self.__array[parent].getData(), self.__array[no].getData()) < 0:
            self.swapNode(parent, no)
            no = parent
            parent = (no - 1) // 2

    cpdef object delete(self):
        cdef HeapNode tmp
        tmp = self.__array[0]
        self.__array[0] = self.__array[self.__count - 1]
        self.percolateDown(0)
        self.__count = self.__count - 1
        return tmp.getData()

    cpdef insert(self, object data):
        if self.__count < self.__N:
            self.__count = self.__count + 1
        self.__array[self.__count - 1] = HeapNode(data)
        self.percolateUp(self.__count - 1)

    def __repr__(self):
        return f"{self.__array}"
