import time

from node import Node


# todo: comment code
#

class Treap:
    def __init__(self):
        self.root = Node()

    def insert(self, key, graph_list):
        self.root = self.root.insert(key, graph_list)

    def find(self, key, graph_list, treap):
        tmp = self.root.find(key, graph_list, treap)
        return tmp

    def delete(self, key, graph_list):
        new_treap = self.root.delete(key, graph_list)
        return new_treap

    def pre_order(self, graph_list):
        self.root.pre_order(graph_list)

    def set_color(self, graph_list):
        self.root = self.root.set_color(graph_list)

