from node import Node
import time


class Treap:
    def __init__(self):
        self.root = Node()

    def insert(self, key, treap, parent=None):
        self.root = self.root.insert(key, treap, parent)
        self.root.clear_colors()

    def find(self, key, treap):
        tmp = self.root.find(key, treap)
        return tmp

    def clear_colors(self):
        self.root.clear_colors()

    def delete(self, key, graph_list, treap):
        new_treap = self.root.delete(key, graph_list, treap)
        return new_treap

    def pre_order(self, graph_list):
        self.root.pre_order(graph_list)

