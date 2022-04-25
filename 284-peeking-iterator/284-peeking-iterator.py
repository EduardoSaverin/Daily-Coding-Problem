class PeekingIterator:
    def __init__(self, iterator):
        self._iterator = iterator
        self._current = None
        self._hasNext = True
        self.next()

    def peek(self):
        return self._current

    def next(self):
        current = self._current
        if self._iterator.hasNext():
            self._current = self._iterator.next()
        else:
            self._hasNext = False
            
        return current

    def hasNext(self):
        return self._hasNext