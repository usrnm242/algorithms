from functools import total_ordering


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


class HashMap(object):
    def __init__(
            self,
            sequence=None,
            key_T=None,
            val_T=None,
            load_factor=2.0,
            hash_func=hash):

        sequence = sequence or []

        self.number_of_elements = len(sequence)
        self.number_of_lists = 2 * self.number_of_elements + 1  # todo
        self.elements = [list() for _ in range(self.number_of_lists)]
        self.hash = hash_func
        self.load_factor = float(load_factor)

        if key_T is not None and val_T is not None:
            self.key_T = key_T
            self.val_T = val_T
        elif len(sequence) == 0:
            raise(IndexError)
        else:
            self.key_T = type(sequence[0][0])
            self.val_T = type(sequence[0][1])

        for key, value in sequence:
            if self._is_valid_type(key, value) and self._has_hash(key):
                index = self._get_index_of(key)
                self.elements[index].append(KeyValue(key, value))
            else:
                raise(SequenceTypeError())

    def _is_valid_type(self, key, value=None) -> bool:
        if not (isinstance(key, self.key_T) and
                hasattr(key, "__lt__") and
                hasattr(key, "__eq__")):
            return False

        if value is not None:
            if not isinstance(value, self.val_T):
                return False

        return True

    def _has_hash(self, item) -> bool:
        if hasattr(item, "__hash__"):
            return True
        else:
            return False

    def change_load_factor(self, load_factor):
        self.load_factor = float(load_factor)

        if not self._load_factor_is_correct():
            self._init_rehashing(2 * self.number_of_lists + 1)

    def current_load_factor(self) -> float:
        return float(self.number_of_elements / self.number_of_lists)

    def _load_factor_is_correct(self) -> bool:
        if self.current_load_factor() < self.load_factor:
            return True
        else:
            return False

    def _init_rehashing(self, new_number_of_lists):
        # checking if we want to minimize number_of_lists:
        if self.number_of_elements / new_number_of_lists > self.load_factor:

            new_number_of_lists = \
                int(self.number_of_elements / self.load_factor)

        self.number_of_lists = new_number_of_lists

        new_elements = [list() for _ in range(self.number_of_lists)]

        for inner_lst in self.elements:
            for item in inner_lst:
                index = self._get_index_of(item.key)
                new_elements[index].append(item)

        self.elements = new_elements

    def _get_index_of(self, key) -> int:
        index = self.hash(key) % self.number_of_lists
        return index

    def append(self, key, value):
        index = self._get_index_of(key)

        item_to_append = KeyValue(key, value)

        if item_to_append in self.elements[index]:
            return

        self.elements[index].append(item_to_append)
        self.number_of_elements += 1

        if not self._load_factor_is_correct():
            self._init_rehashing(2 * self.number_of_lists + 1)

    def __iter__(self):
        for i in self.elements:
            yield i

    def __getitem__(self, key):  # get value by key
        if self._is_valid_type(key):
            index = self._get_index_of(key)
            item_to_search = KeyValue(key)

            for item in self.elements[index]:
                if item_to_search == item:
                    return item.value

            return None

        else:
            raise(SequenceTypeError)

    def __setitem__(self, key, new_value):  # set value by key
        if self._is_valid_type(key, new_value):
            index = self._get_index_of(key)

            item_to_change = KeyValue(key, new_value)

            for item in self.elements[index]:
                if item_to_change == item:
                    item.value = new_value
                    return

            # if there is no key like that then append new item
            self.elements[index].append(item_to_change)
            self.number_of_elements += 1

            if not self._load_factor_is_correct():
                self._init_rehashing(2 * self.number_of_lists + 1)

            return

        else:
            raise(SequenceTypeError)

    def __missing__(self, key):
        return None

    def __delitem__(self, key):
        if self._is_valid_type(key):
            index = self._get_index_of(key)

            item_to_delete = KeyValue(key)

            for inner_index, item in enumerate(self.elements[index]):
                if item_to_delete == item:
                    del self.elements[index][inner_index]
                    return

        else:
            raise(SequenceTypeError)


def main():
    a = HashMap([('1', 0), ('2', 0), ('3', 0)])

    for i in a:
        print(i)
    print('_' * 40)

    a.change_load_factor(0.35)
    # a._init_rehashing(1)

    print("after changing")

    for i in a:
        print(i)
    print('_' * 40)

    a['4'] = 145

    del a['4']

    for i in a:
        print(i)


if __name__ == '__main__':
    main()
