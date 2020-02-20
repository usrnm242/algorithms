from functools import total_ordering


def christmas_tree(height):
    for i in range(height, 0, -1):
        print(' ' * (i - 1), '*' * (2 * (height - i) + 1), sep='')


class SequenceTypeError(TypeError):
    def __init__(self, error="Elements in sequence must be the same type."):
        self.error = error


class Heapq(object):
    """docstring for Heap"""

    def __init__(self):
        self.heap = []
        self.size = 0

    def __repr__(self):
        return str(self.heap)

    def left_child_index(self, i):
        return i * 2 + 1

    def right_child_index(self, i):
        return i * 2 + 2

    def heappush(self, arg):
        self.heap.append(arg)
        self.size += 1
        return self.size

    def heappop(self):
        self.size -= 1
        return self.heap.pop()

    def is_empty(self) -> bool:
        return self.size == 0

    def heap_size(self) -> int:
        return self.size

    def heapify(self, i):
        parent = i

        while True:
            left_child = self.left_child_index(parent)
            right_child = self.right_child_index(parent)
            candidate = i

            if left_child < self.size and self.heap[left_child] > self.heap[candidate]:
                candidate = left_child

            if right_child < self.size and self.heap[right_child] > self.heap[candidate]:
                candidate = left_child

            if candidate == parent:
                print("break", i)
                break

            # swap
            self.heap[candidate], self.heap[parent] = \
                self.heap[parent], self.heap[candidate]

            parent = candidate

    def build_heap(self):
        for i in range(len(self.heap) // 2, -1, -1):
            # print(i)
            self.heapify(i)


class PriorityQueue(object):

    def __init__(self, sequence, *args):
        sequence = list(sequence)
        sequence.extend(args)

        self.heap = Heapq()
        self.T = type(sequence[0])

        try:
            for element in sequence:
                if isinstance(element, self.T) and hasattr(element, "__lt__"):
                    self.heap.heappush(element)
                else:
                    raise(SequenceTypeError())
        except SequenceTypeError as e:
            raise(e)

        self.heap.build_heap()

    def __repr__(self):
        return str(self.heap)

    # here
    def push(self, element):
        if isinstance(element, self.T) and hasattr(element, "__lt__"):
            return self.heap.heappush(element)

    # here
    def pop(self):
        return self.heap.heappop()


@total_ordering
class Person(object):
    def __init__(self, name="No Name", age=0):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __repr__(self):
        return '(' + str(self.name) + '; ' + str(self.age) + ')'


lst = [1,2,3,4,-1,0,100]
# lst = {1: 1, 2: 2, 3: 3}
# lst = [Person(), Person("Max", 11)]
q = PriorityQueue(lst)
# q.push(500)
# a = q.pop()
print(q)








