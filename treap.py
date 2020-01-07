
from node import Node
import treap_graph as tr


# todo: comment code
#

class Treap:
    def __init__(self):
        self.root = Node()

    def insert(self, key, graph_list, treap, parent=None):
        self.root = self.root.insert(key, graph_list, treap, parent)

    def find(self, key, graph_list, treap):
        tmp_graph = tr.TreapGraph(treap)
        self.root.clear_colors()
        graph_list.append(tmp_graph.create_graph())
        tmp = self.root.find(key, graph_list, treap)
        return tmp

    def clear_colors(self):
        self.root.clear_colors()

    def delete(self, key, graph_list, treap):
        new_treap = self.root.delete(key, graph_list, treap)
        return new_treap

    def pre_order(self, graph_list):
        self.root.pre_order(graph_list)

    def set_color(self, graph_list):
        self.root = self.root.set_color(graph_list)
