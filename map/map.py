class SequenceTypeError(TypeError):
    """Error appears when we've got different typesof obj in sequence"""

    def __init__(self, error="Elements in sequence must be the same type."):
        self.error = error


class Comparator(object):

    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def compare(self, func):
        return func(self.arg1) < func(self.arg2)


class Map(object):

    def __init__(self, sequence=[], comparator=min, key_T=None, val_T=None):
        self.keys = []
        self.values = []

        if key_T is not None and val_T is not None:
            self.key_T = key_T
            self.val_T = val_T
        elif len(sequence) == 0:
            raise(IndexError)
        else:
            self.key_T = type(sequence[0][0])
            self.val_T = type(sequence[0][1])

        for key, value in sequence:
            if isinstance(key, self.key_T) and hasattr(key, "__lt__"):
                self.keys.append(key)
            else:
                raise(SequenceTypeError())

            if isinstance(value, self.val_T):
                self.values.append(value)
            else:
                raise(SequenceTypeError())

    def __repr__(self):
        return str(self.keys) + '\n' + str(self.values)


lst = [(1, '3'), (2, '4')]
m = Map(lst, key_T=int, val_T=str)
print(m)

print(Comparator(-1, 0).compare(lambda x: x ** 3))
