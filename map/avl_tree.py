class BinaryNode():
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

    def compute_height(self):
        height = -1

        if self.left:
            height = max(height, self.left.height)

        if self.right:
            height = max(height, self.right.height)

        self.height = height + 1

    def dynamic_height(self):
        height = -1

        if self.left:
            height = max(height, self.left.dynamic_height())

        if self.right:
            height = max(height, self.right.dynamic_height())

        return height + 1

    def dynamic_height_difference(self):
        leftTarget = 0
        rightTarget = 0

        if self.left:
            leftTarget = 1 + self.left.dynamic_height()

        if self.right:
            rightTarget = 1 + self.right.dynamic_height()

        return leftTarget - rightTarget

    def height_difference(self):
        # difference of node's children
        leftTarget = 0
        rightTarget = 0

        if self.left:
            leftTarget = 1 + self.left.height

        if self.right:
            rightTarget = 1 + self.right.height

        return leftTarget - rightTarget

    def rotate_right(self):
        new_root = self.left
        grandson = new_root.right

        self.left = grandson
        new_root.right = self

        self.compute_height()
        return new_root

    def rotate_left(self):
        new_root = self.right
        grandson = new_root.left

        self.right = grandson
        new_root.left = self

        self.compute_height()
        return new_root

    def rotate_left_right(self):
        child = self.left
        new_root = child.right

        grand1 = new_root.left
        grand2 = new_root.right

        child.right = grand1
        self.left = grand2

        new_root.left = child
        new_root.right = self

        child.compute_height()
        self.compute_height()

        return new_root

    def rotate_right_left(self):
        child = self.right
        new_root = child.left

        grand1 = new_root.left
        grand2 = new_root.right

        child.left = grand2
        self.right = grand1

        new_root.left = self
        new_root.right = child

        child.compute_height()
        self.compute_height()

        return new_root

    def add(self, val):
        new_root = self

        if val <= self.value:
            self.left = self.add_to_subtree(self.left, val)
            if self.height_difference() == 2:
                if val <= self.left.value:
                    new_root = self.rotate_right()
                else:
                    new_root = self.rotate_left_right()
        else:
            self.right = self.add_to_subtree(self.right, val)
            if self.height_difference() == -2:
                if val > self.right.value:
                    new_root = self.rotate_left()
                else:
                    new_root = self.rotate_right_left()

        new_root.compute_height()

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

            if self.height_difference() == -2:
                if self.right.height_difference() <= 0:
                    new_root = self.rotate_left()
                else:
                    new_root = self.rotate_right_left()

        elif self.value > val:
            self.left = self.remove_from_parent(self.left, val)
            if self.height_difference() == -2:
                if self.right.height_difference() <= 0:
                    new_root = self.rotate_left()
                else:
                    new_root = self.rotate_right_left()

        else:
            self.right = self.remove_from_parent(self.right, val)
            if self.height_difference() == 2:
                if self.left.height_difference() >= 0:
                    new_root = self.rotate_right()
                else:
                    new_root = self.rotate_left_right()

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
        return self.root == None

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
