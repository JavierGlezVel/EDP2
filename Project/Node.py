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
        else:
            return node.parent.parent.left
