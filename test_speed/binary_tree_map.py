from functools import total_ordering
from binary_tree import BinaryTree


class SequenceTypeError(TypeError):
    """Error appears when we've got different types of obj in sequence"""

    def __init__(self, error="Elements in sequence must be the same type."):
        self.error = error


# no needed, but I'll show you 'one more thing' :)
class Comparator(object):

    def __init__(self, arg1, arg2, func):
        self.arg1 = arg1
        self.arg2 = arg2
        self.func = func

    def compare(self):
        try:
            return self.func(self.arg1) < self.func(self.arg2)
        except Exception as e:
            raise(e)


class KeyValueBinaryTree(BinaryTree):
    """Extending simple BinaryTree for using key-value"""

    def __init__(self):
        super().__init__()

    def get_by_key(self, key):
        node = self.root

        while node:
            if node.value.key == key:
                return node.value.value
            elif node.value.key > key:
                node = node.left
            else:
                node = node.right

        return None

    def set_by_key(self, key, new_value):
        node = self.root

        while node:
            if node.value.key == key:
                node.value.value = new_value
                return
            elif node.value.key > key:
                node = node.left
            else:
                node = node.right


class Map(object):

    @total_ordering
    class KeyValue(object):
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __eq__(self, other):
            return self.key == other.key

        def __lt__(self, other):
            return self.key < other.key

        def __repr__(self):
            return '(' + str(self.key) + ': ' + str(self.value) + ')'

    def __init__(
            self,
            sequence=[],
            key_T=None,
            val_T=None,
            compare_func=lambda x: x):

        self.tree = KeyValueBinaryTree()

        self.compare = lambda x, y: Comparator(x, y, compare_func).compare()

        # check for testing:
        # print(self.compare(2, -3), "is result of comparing 2 and -3")

        if key_T is not None and val_T is not None:
            self.key_T = key_T
            self.val_T = val_T
        elif len(sequence) == 0:
            raise(IndexError)
        else:
            self.key_T = type(sequence[0][0])
            self.val_T = type(sequence[0][1])

        for key, value in sequence:
            if self._is_valid_type(key, value):
                self.tree.append(self.KeyValue(key, value))
            else:
                raise(SequenceTypeError())

    def _is_valid_type(self, key, value=None):
        if not (isinstance(key, self.key_T) and
                hasattr(key, "__lt__") and
                hasattr(key, "__eq__")):
            return False

        if value is not None:
            if not isinstance(value, self.val_T):
                return False

        return True

    def append(self, key, value):
        if self._is_valid_type(key, value):
            self.tree.append(self.KeyValue(key, value))
        else:
            raise(SequenceTypeError())

    def is_empty(self):
        return self.tree.is_empty()

    def __repr__(self):
        return str(self.tree)

    def __iter__(self):
        for i in self.tree:
            yield i

    def __getitem__(self, key):
        if self._is_valid_type(key):
            return self.tree.get_by_key(key)
        else:
            raise(SequenceTypeError)

    def __setitem__(self, key, value):
        if self._is_valid_type(key, value):
            return self.tree.set_by_key(key, value)
        else:
            raise(SequenceTypeError)

    def __missing__(self, key):
        return None

    def __delitem__(self, key):
        if self._is_valid_type(key):
            return self.tree.del_by_key(key)
        else:
            raise(SequenceTypeError)


# m = Map(lst, key_T=int, val_T=int)  #, compare_func=lambda x: x ** 2)
