from node import Node


class Treap:
    def __init__(self):
        self.root = Node()

    def insert(self, key, treap, parent=None):
        self.root.insert(key, treap, parent)

    def find(self, key, treap, log_message):
        self.root.find(key, treap, log_message)

    def clear_colors(self):
        self.root.clear_colors()

    def delete(self, key, treap):
        self.root.delete(key, treap)

