class Node:
    def __init__(self, key, color='black'):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = color
