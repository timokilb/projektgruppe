import time

import networkx as nx


class TreapGraph:
    def __init__(self, treap):
        self.graph = nx.Graph()
        self.treap = treap

    def create_graph(self):
        graph = nx.Graph()
        self.draw_treap(self.treap.root, graph, 1, 0)
        return graph

    def draw_treap(self, node, graph, xpos, ypos):
        if node.key is None:
            graph.add_node(node.key, pos=(xpos, ypos), label=node.key,
                           color=node.color)
        else:
            graph.add_node(node.key, pos=(xpos, ypos), label=str(node.key) + "\n" + str(node.priority),
                           color=node.color)
        if node.parent_node:
            graph.add_edge(node.key, node.parent_node.key)
        node.xpos = xpos  # Set position of node for recursive callback
        if node.left_node is not None:  # Drawing a left child
            if node.parent_node is None:  # Root case
                self.draw_treap(node.left_node, graph, xpos - (xpos) / 2, ypos - 1)
            else:
                self.draw_treap(node.left_node, graph, xpos - abs(xpos - node.parent_node.xpos) / 2, ypos - 1)

        if node.right_node is not None:  # Drawing a right child
            if node.parent_node is None:  # Root case
                self.draw_treap(node.right_node, graph, xpos + (xpos) / 2, ypos - 1)
            else:
                self.draw_treap(node.right_node, graph, xpos + abs(xpos - node.parent_node.xpos) / 2, ypos - 1)
        else:
            return

    def draw(self, treap, plot, canvas):
        plot.clear()
        self.treap = treap
        self.graph = self.create_graph()
        pos = nx.get_node_attributes(self.graph, 'pos')
        label = nx.get_node_attributes(self.graph, 'label')
        color_dict = nx.get_node_attributes(self.graph, 'color')
        color_list = []
        for color in color_dict:
            color_list.append(color_dict[color])
        nx.draw(self.graph, pos, node_size=1000, node_color=color_list, labels=label, with_labels=True, ax=plot)
        canvas.draw()
