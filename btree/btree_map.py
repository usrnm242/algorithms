from functools import total_ordering
from btree import BTree
from binary_search import bisect_right



class SequenceTypeError(TypeError):
    """Error appears when we've got different types of obj in sequence"""

    def __init__(self, error="Elements in sequence must be the same type."):
        self.error = error


@total_ordering
class KeyValue(object):
    def __init__(self, key, value=None):
        self.key = key
        self.value = value

    def __eq__(self, other):
        if self.value is not None:
            return self.key == other.key and self.value == other.value
        else:
            return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key

    def __repr__(self):
        return '(' + str(self.key) + ': ' + str(self.value) + ')'


class KeyValueBTree(BTree):
    """Extending BTree for using key-value"""

    def __init__(self, t):
        super().__init__(t)

    def __contains__(self, key):
        current_node = self.root

        if key.value is not None:
            while True:
                i = bisect_right(current_node.keys, key) - 1

                if i >= 0 and current_node.keys[i] == key:
                    return True
                elif current_node.is_leaf:
                    return False
                else:
                    current_node = current_node.children[i + 1]

        else:
            while True:
                i = bisect_right([i.key for i in current_node.keys],
                                 key.key) - 1

                if i >= 0 and current_node.keys[i].key == key.key:
                    return True
                elif current_node.is_leaf:
                    return False
                else:
                    current_node = current_node.children[i + 1]

    def get_by_key(self, key):
        current_node = self.root
        item_to_get = KeyValue(key)

        while True:
            i = bisect_right([i.key for i in current_node.keys], key) - 1

            if i >= 0 and item_to_get == current_node.keys[i]:
                return current_node.keys[i].value
            elif current_node.is_leaf:
                return None
            else:
                current_node = current_node.children[i + 1]

        return None

    def set_by_key(self, key, new_value):
        current_node = self.root

        while True:
            i = bisect_right([i.key for i in current_node.keys], key) - 1

            if i >= 0 and current_node.keys[i].key == key:
                current_node.keys[i].value = new_value
                return True
            elif current_node.is_leaf:
                return False
            else:
                current_node = current_node.children[i + 1]

        return False

    def _remove_key(self, node, key) -> bool:
        try:
            key_index = [item.key for item in node.keys].index(key)
            if node.is_leaf:
                node.keys.pop(key_index)
                return True
            else:
                self._remove_from_nonleaf_node(node, key_index)

            return True

        except ValueError:  # key not found in node
            if node.is_leaf:
                print("Key not found.")
                return False  # key not found
            else:
                i = 0
                number_of_keys = len(node.keys)
                while i < number_of_keys and \
                        key > node.keys[i].key:
                    # decide in which subtree may be key
                    i += 1

                action_performed = self._repair_tree(node, i)
                if action_performed:
                    return self._remove_key(node, key)
                else:
                    return self._remove_key(node.children[i], key)

    def remove_key(self, key):
        return self._remove_key(self.root, key)


class Map(object):
    def __init__(
            self,
            sequence=[],
            t=2,
            key_T=None,
            val_T=None,
            compare_func=lambda x: x):

        self.tree = KeyValueBTree(t)

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
                is_set = self.tree.set_by_key(key, value)

                if not is_set:
                    # if there is no key like that then append new item
                    self.tree.insert_key(KeyValue(key, value))

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
            self.tree.insert_key(KeyValue(key, value))
        else:
            raise(SequenceTypeError())

    def is_empty(self):
        return self.tree.is_empty()

    def __getitem__(self, key):
        if self._is_valid_type(key):
            return self.tree.get_by_key(key)
        else:
            raise(SequenceTypeError)

    def __setitem__(self, key, new_value):
        if self._is_valid_type(key, new_value):
            is_set = self.tree.set_by_key(key, new_value)

            if not is_set:
                # if there is no key like that then append new item
                self.tree.insert_key(KeyValue(key, new_value))

        else:
            raise(SequenceTypeError)

    def __missing__(self, key):
        return None

    def __delitem__(self, key):
        if self._is_valid_type(key):
            return self.tree.remove_key(key)
        else:
            raise(SequenceTypeError)

    def __iter__(self):
        for i in self.tree:
            yield i

    def __len__(self):
        return len(self.tree)

    def __contains__(self, value):
        if not isinstance(value, KeyValue):
            try:
                value = KeyValue(value[0], value[1]) if isinstance(value, tuple) else KeyValue(value)
            except TypeError:
                raise(SequenceTypeError)
        return value in self.tree

    def __repr__(self):
        return self.tree.__repr__()
