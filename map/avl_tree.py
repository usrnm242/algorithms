class BinaryNode(object):

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

        self.height += 1

    def height_difference(self):
        left_target = 0
        right_target = 0

        if self.left:
            left_target = 1 + self.left.height

        if self.right:
            right_target = 1 + self.right.height

        return left_target - right_target

    def add_node(self, value):
        new_root = self

        if value <= self.value:
            self.left = self.add_to_subtree(self.left, value)

            if self.height_difference() == 2:

                if value <= self.left.value:
                    new_root = self.rotate_right()
                else:
                    new_root = self.rotate_left_right()

        else:
            self.right = self.add_to_subtree(self.right, value)

            if self.height_difference() == -2:

                if value > self.right.value:
                    new_root = self.rotate_left()
                else:
                    new_root = self.rotate_right_left()

        new_root.compute_height()

        return new_root

    def add_to_subtree(self, parent, value):
        if parent is None:
            return BinaryNode(value)

        parent = parent.add_node(value)

        return parent

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

    def rotate_right_left(self):
        child = self.right
        new_root = child.left

        grandson1 = new_root.left
        grandson2 = new_root.right

        child.left = grandson2
        child.right = grandson1

        new_root.left = self
        new_root.right = child

        child.compute_height()
        self.compute_height()

        return new_root

    def rotate_left_right(self):
        child = self.left
        new_root = child.right

        grandson1 = new_root.left
        grandson2 = new_root.right

        child.left = grandson1
        child.right = grandson2

        new_root.left = child
        new_root.right = self

        child.compute_height()
        self.compute_height()

        return new_root




class BinaryTree(object):

    def __init__(self):
        self.root = None

    def empty(self):
        return self.root is None

    def add(self, value):
        if self.empty():
            self.root = BinaryNode(value)
        else:
            self.root.add_node(value)

    def __contains__(self, target):
        node = self.root

        while node:
            if target < node.value:
                node = node.left
            elif target > node.value:
                node = node.right
            else:
                return True

        return False


tree = BinaryTree()
tree.add(5)
tree.add(10)
tree.add(15)
print(5 in tree)
