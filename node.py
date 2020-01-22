import random
import math
import time
from tkinter import messagebox
import treap_graph as tr
import animation_handler as ah


class Node:

    def __init__(self, key=None, parent=None):
        self.key = key
        if key == 666:
            self.priority = 1000
        else:
            self.priority = random.randint(1, 1001)  # spezial case check smaller
        self.left_node = None
        self.right_node = None
        self.parent_node = parent
        self.xpos = 0
        self.color = "palegreen"

    def insert(self, key, treap, parent=None):
        animation_handler = ah.AnimationHandler()
        tmp_graph = tr.TreapGraph(treap)
        tmp = self

        # pseudo should start at top
        if self.parent_node is None:
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 0)

        # TODO ÜBERLEGEN OB SO GEWOLLT
        if key == self.key:
            while tmp.parent_node:
                tmp = tmp.parent_node
            tmp.find(key, treap)
            return

        if self.key is None:
            self.color = "red"
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 2)
            self.key = key
            self.color = "palegreen"
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 3)

        elif key <= self.key:
            self.color = "grey"
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 4)
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 5)

            if not self.left_node:
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 2)
                self.left_node = Node(key, self)
                self.left_node.color = "red"
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 3)
                self.left_node.color = "palegreen"
                if self.left_node.priority > self.priority:
                    tmp = self.left_node.rotate_right(treap)
                self.default_color()
                print()
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 0)
            else:

                self.left_node.insert(key, treap, self)

        else:
            self.color = "grey"
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 8)
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 9)

            if not self.right_node:
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 2)
                self.right_node = Node(key, self)
                self.right_node.color = "red"
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 3)
                self.right_node.color = "palegreen"
                if self.right_node.priority > self.priority:
                    tmp = self.right_node.rotate_left(treap)
                self.default_color()
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 0)
            else:
                self.right_node.insert(key, treap, self)
        while tmp.parent_node:
            tmp = tmp.parent_node
        tmp.default_color()

    def find(self, key, treap):

        if self.key is None:
            return self
        animation_handler = ah.AnimationHandler()
        tmp_graph = tr.TreapGraph(treap)

        if self.parent_node is None:
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 0)
        if self.key == key:
            tmp = self
            tmp.color = "red"
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 2)
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 3)
            return tmp
        elif key <= self.key:
            if self.left_node:
                self.color = "grey"
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 4)
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 5)
                tmp = self.left_node.find(key, treap)
            else:
                return self
        else:
            if self.right_node:
                self.color = "grey"
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 6)
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 7)
                tmp = self.right_node.find(key, treap)
            else:
                # messagebox.showinfo("Error in find", f"Treap does not contain : {key}")
                return self
            while tmp.parent_node:
                tmp.color = "palegreen"
                tmp = tmp.parent_node
            tmp.color = "palegreen"
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 0)

        return tmp

    def find_node(self, key):
        if self.key == key:
            return self
        elif key > self.key:
            return self.right_node.find_node(key)
        elif key <= self.key:
            return self.left_node.find_node(key)

    # Todo: Cases checken , problems with deleting the root !!! rotations are working abs. fine
    def delete(self, key, treap):
        animation_handler = ah.AnimationHandler()
        tmp_graph = tr.TreapGraph(treap)
        animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 0)
        animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 2)
        self.find(key, treap)
        tmp = self.find_node(key)
        tmp.color = "red"
        animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 2)

        # Case 1 : node to be deleted is a Leaf
        if tmp.left_node is None and tmp.right_node is None:
            # Node to be deleted is not Root
            if tmp.parent_node is not None:
            # Node is left-Node from Parents perspective
                tmp.color = "red"
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 4)

                if tmp.parent_node.left_node == tmp:
                    tmp.parent_node.left_node = None
                    tmp.color = "palegreen"
                    animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 5)
                    return
                # Node is right_node from Parents perspective
                else:
                    tmp.parent_node.right_node = None
                    animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 5)
                    return
            # Node is Root
            else:
                tmp.key = None
                tmp.priority = random.randint(1, 1001)  # sonst wird nur key gelöscht prio w+rde gleich bleiebn ohne
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 5)
                return
        else:
            tmp.priority = -math.inf
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 3)
            if tmp.left_node is None:
                tmp.right_node.rotate_left(treap)
                tmp.delete(key, treap)
                return
            elif tmp.right_node is None:
                tmp.left_node.rotate_right(treap)
                tmp.delete(key, treap)
                return
            else:
                tmp.move_down(treap)
                tmp.delete(key, treap)
                return
        return
    # Moving a Node trough left/right rotation down
    def move_down(self, treap):
        if self.left_node.priority > self.right_node.priority:
            self.left_node.rotate_right(treap)
        elif self.right_node.priority > self.left_node.priority:
            self.right_node.rotate_left(treap)

    def rotate_left(self, treap):
        animation_handler = ah.AnimationHandler()
        tmp_graph = tr.TreapGraph(treap)
        # self ist der zu rotierende Knoten
        self.color = "red"
        if self.parent_node:
            self.parent_node.color = "orange"
        if self.left_node:
            self.left_node.color = "lightblue"
        animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 11)

        if self.parent_node.parent_node is not None:  # Tief im Baum
            if self.parent_node == self.parent_node.parent_node.left_node:  # Parent ist left child
                self.parent_node.parent_node.left_node = self
            elif self.parent_node == self.parent_node.parent_node.right_node:  # Parent ist right child
                self.parent_node.parent_node.right_node = self

        if self.left_node is not None:  # Left child
            self.left_node.parent_node = self.parent_node

        self.parent_node.right_node = self.left_node
        self.left_node = self.parent_node
        self.parent_node = self.parent_node.parent_node
        self.left_node.parent_node = self
        if self.parent_node is None:
            treap.root = self
        animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 11)
        self.left_node.color = "palegreen"
        animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 11)
        if self.parent_node is not None and self.priority > self.parent_node.priority:
            if self.parent_node.left_node == self:
                self.rotate_right(treap)
            else:
                self.rotate_left(treap)
        self.color = "palegreen"
        self.clear_colors()
        animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 11)
        return self

    def rotate_right(self, treap):
        animation_handler = ah.AnimationHandler()
        tmp_graph = tr.TreapGraph(treap)
        # self ist der zu rotierende Knoten
        self.color = "red"
        if self.parent_node:
            self.parent_node.color = "orange"
        if self.right_node:
            self.right_node.color = "lightblue"
        animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 7)

        if self.parent_node.parent_node is not None:
            if self.parent_node == self.parent_node.parent_node.left_node:
                self.parent_node.parent_node.left_node = self
            elif self.parent_node == self.parent_node.parent_node.right_node:  # Parent ist right child
                self.parent_node.parent_node.right_node = self

        if self.right_node is not None:
            self.right_node.parent_node = self.parent_node

        self.parent_node.left_node = self.right_node
        self.right_node = self.parent_node
        self.parent_node = self.parent_node.parent_node
        self.right_node.parent_node = self

        if self.parent_node is None:
            treap.root = self

        animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 7)
        self.right_node.color = "palegreen"
        animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 7)
        if self.parent_node is not None and self.priority > self.parent_node.priority:
            if self.parent_node.left_node == self:
                self.rotate_right(treap)
            else:
                self.rotate_left(treap)
        self.color = "palegreen"
        self.clear_colors()
        animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 7)
        return self

    def pre_order(self, graph_list):
        if self:
            print(self.key)
            # print("level : ", self.level, "key : ", self.key, "prio : ", self.priority)
        if self.left_node:
            # print("left :")
            self.left_node.pre_order(graph_list)
        if self.right_node:
            # print("right : ")
            self.right_node.pre_order(graph_list)

    def clear_colors(self):
        if self:
            self.color = "palegreen"
            return self
        if self.left_node:
            return self.left_node.clear_colors()
        if self.right_node:
            return self.right_node.clear_colors()

    def default_color(self):
        tmp = self
        while tmp.parent_node:
            tmp.color = "palegreen"
            tmp = tmp.parent_node
        tmp.color = "palegreen"
