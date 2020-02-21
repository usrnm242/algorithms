def christmas_tree(height):
    # mood :)
    for i in range(height, 0, -1):
        print(' ' * (i - 1), '*' * (2 * (height - i) + 1), sep='')


class SequenceTypeError(TypeError):
    """Error appears when we've got different typesof obj in sequence"""

    def __init__(self, error="Elements in sequence must be the same type."):
        self.error = error


class Heapq(object):

    def __init__(self, comparsion_type):
        self.heap = []
        self.size = 0
        self.compare = comparsion_type  # min heap or max heap

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

    def heappush(self, arg) -> int:
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
    def __init__(self, sequence, *args, key=min, seq_type=None):
        sequence = list(sequence)
        sequence.extend(args)

        if len(sequence) == 0 and seq_type is not None:
            self.T = seq_type
        elif len(sequence) == 0 and seq_type is None:
            raise(IndexError)
        else:
            self.T = type(sequence[0])

        self.heap = Heapq(key)

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

    def is_empty(self) -> bool:
        return self.heap.size == 0

    def heap_size(self) -> int:
        return self.heap.size

    def peek(self):
        if not self.is_empty():
            return self.heap.heap[0]
        else:
            raise(IndexError)

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
