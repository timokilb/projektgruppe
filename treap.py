from node import Node


# todo: comment code
#

class Treap:
    def __init__(self):
        self.root = Node()

    def insert(self, key, graph_list):
        self.root = self.root.insert(key, graph_list)

    def find(self, key):
        tmp = self.root.find(key)
        return tmp

    def delete(self, key):
        new_treap = self.root.delete(key)
        return new_treap

    def pre_order(self, graph_list):
        self.root.pre_order(graph_list)


if __name__ == "__main__":
    test = Treap()
    graph = 5
    data = open("data.txt", "r")

    for line in range(1,4):
        test.insert(int(line), graph)

    test.delete(test.root.key)




