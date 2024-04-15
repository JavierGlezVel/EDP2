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