cdef class HeapNode:

    def __init__(self, data: object):
        self.__data = data

    cpdef object getData(self):
        return self.__data

    def __repr__(self):
        return f"{self.__data}"
