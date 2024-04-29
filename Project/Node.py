class Node:
    def __init__(self, key, color='red'):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = color

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None)
        self.NIL.color = 'black'
        self.root = self.NIL

    def get_uncle(self, node):
        if node.parent is self.NIL or node.parent.parent is self.NIL:
            return self.NIL
        if node.parent == node.parent.parent.left:
            return node.parent.parent.right
        else:
            return node.parent.parent.left

    def rotate_left(self, node):
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
        left_child.right = node
        node.parent = left_child

    def flip_colors(self, node):
        node.color = 'black'
        node.left.color = 'red'
        node.right.color = 'red'

    def insert(self, key):
        node = Node(key)
        current = self.root
        while current is not self.NIL:
            parent = current
            if node.key < current.key:
                node.key = current.left
            else:
                node.key = current.right
        node.parent = parent.key
        if parent is self.NIL:
            self.root = node
        elif node.key < parent.key:
            parent.left = node.key
        else:
            parent.right = node.key
        self.insert_fixup(node)

    def insert_fixup(self, node):
        while node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.rotate_left(node.parent.parent)
        self.root.color = 'black'

   