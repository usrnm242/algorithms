class BinaryNode():
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def add(self, val):
        new_root = self

        if val <= self.value:
            self.left = self.add_to_subtree(self.left, val)

        else:
            self.right = self.add_to_subtree(self.right, val)

        return new_root

    def add_to_subtree(self, parent, val):
        if parent is None:
            return BinaryNode(val)

        parent = parent.add(val)

        return parent

    def remove_from_parent(self, parent, val):
        if parent:
            return parent.remove(val)
        return None

    def remove(self, val):
        new_root = self

        if self.value == val:
            if self.left is None:
                return self.right

            child = self.left
            while child.right:
                child = child.right

            child_key = child.value

            self.left = self.remove_from_parent(self.left, child_key)
            self.value = child_key

        elif self.value > val:
            self.left = self.remove_from_parent(self.left, val)

        else:
            self.right = self.remove_from_parent(self.right, val)

        new_root.compute_height()
        return new_root

    def inorder(self):
        if self.left:
            for v in self.left.inorder():
                yield v

        yield self.value

        if self.right:
            for v in self.right.inorder():
                yield v


class BinaryTree():

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def append(self, value):
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root = self.root.add(value)

    def __contains__(self, target):
        node = self.root

        while node:
            if node.value == target:
                return True
            elif node.value > target:
                node = node.left
            else:
                node = node.right

        return False

    def remove(self, val):
        if self.root:
            self.root = self.root.remove(val)

    def __iter__(self):
        if self.root:
            for e in self.root.inorder():
                yield e
