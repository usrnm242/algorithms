from functools import total_ordering


def christmas_tree(height):
    for i in range(height, 0, -1):
        print(' ' * (i - 1), '*' * (2 * (height - i) + 1), sep='')


class SequenceTypeError(TypeError):
    def __init__(self, error="Elements in sequence must be the same type."):
        self.error = error


class Heapq(object):
    def __init__(self, comparsion_type):
        self.heap = []
        self.size = 0
        self.compare = comparsion_type

    def __repr__(self):
        return str(self.heap)

    def left_child_index(self, i):
        return i * 2 + 1

    def right_child_index(self, i):
        return i * 2 + 2

    def parent_index(self, i):
        return (i - 1) // 2

    def sift_up(self, i):
        child = i
        parent = self.parent_index(i)

        while child > 0 and self.compare(self.heap[child], self.heap[parent]) == self.heap[child]:
            self.swap_by_index(child, parent)
            child = parent
            parent = self.parent_index(child)

    def heappush(self, arg):
        self.size += 1
        self.heap.append(arg)
        self.sift_up(self.size - 1)
        return self.size

    def heappop(self):
        if self.size < 1:
            raise(IndexError)
        else:
            max_element = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self.size -= 1
            self.heapify(0)
            return max_element

    def is_empty(self) -> bool:
        return self.size == 0

    def get_size(self) -> int:
        return self.size

    def swap_by_index(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def heapify(self, i):
        parent = i
        heap = self.heap
        compare = self.compare

        while True:
            left_child = self.left_child_index(parent)
            right_child = self.right_child_index(parent)
            candidate = parent

            try:

                if left_child < self.size and \
                        compare(heap[left_child], heap[candidate]) == heap[left_child]:

                    candidate = left_child

                if right_child < self.size and \
                        compare(heap[right_child], heap[candidate]) == heap[right_child]:

                    candidate = right_child

            except Exception as e:
                raise(e)

            if candidate == parent:
                break

            # swap
            self.swap_by_index(candidate, parent)

            parent = candidate

    def build_heap(self):
        for i in range(len(self.heap) // 2, -1, -1):
            self.heapify(i)


class PriorityQueue(object):
    def __init__(self, sequence, *args, key=min):
        sequence = list(sequence)
        sequence.extend(args)

        self.heap = Heapq(key)
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
        try:
            if isinstance(element, self.T) and hasattr(element, "__lt__"):
                return self.heap.heappush(element)
            else:
                raise(SequenceTypeError)
        except SequenceTypeError as e:
            raise(e)

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


lst = [1, 2, 3, 4, 0, 100]
# lst = [Person("", 1), Person("", 2), Person("", 3), Person("", 4), Person("", 0), Person("", 100)]

q = PriorityQueue(lst, key=max)

q.push(5)
# a = q.pop()
print(q)








