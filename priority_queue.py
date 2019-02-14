import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0 # record order of element insert

    def push(self, element, priority):
        heapq.heappush(self._queue, (-priority, self._index, element))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

if __name__ == '__main__':
    q = PriorityQueue()

    q.push(Item('foo'), 1)
    q.push(Item('bar'), 2)

    print(q.pop())
    print(q.pop())
