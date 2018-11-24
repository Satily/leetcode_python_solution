from data_structure import Iterator


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.__iterator = iterator
        self.__next_elem = None
        self.__refresh_next()

    def __refresh_next(self):
        if self.__iterator.hasNext():
            self.__next_elem = self.__iterator.next()
        else:
            self.__next_elem = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.__next_elem

    def next(self):
        """
        :rtype: int
        """
        result = self.__next_elem
        self.__refresh_next()
        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.__next_elem is not None


if __name__ == "__main__":
    iterator = Iterator([1, 2, 3])
    peeking_iterator = PeekingIterator(iterator)
    print(peeking_iterator.next())
    print(peeking_iterator.peek())
    print(peeking_iterator.next())
    print(peeking_iterator.next())
    print(peeking_iterator.hasNext())
