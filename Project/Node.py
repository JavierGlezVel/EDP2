class Node:
    def __init__(self, key, color='red'):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = color


class ReedBlackTree:
    def __init__(self):
        self.NIL = Node(None)
        self.NIL.color = 'black'
        self.root = self.NIL

    def get_uncle(self, node):
        if node.parent is self.NIL or node.parenta.parent is self.NIL:
            return self.NIL
        if node.parent == node.parent.parent.left:
            return node.parent.parent.right
        return node.parent.parent.left

    def rotate_lef(self, node):
        right_child = node.right
        node.right = right_child.left
        if node.right is not self.NIL:
            node.right.parent = node
        right_child.parent = node.parent
        if node.parent is self.NIL:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        if node.left is not self.NIL:
            node.left.parent = node
        left_child.parent = node.parent
        if node.parent is self.NIL:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.rigth = node
        node.parent = left_child