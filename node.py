import random
import math
from tkinter import messagebox
import treap_graph as tr
import animation_handler as ah


class Node:

    def __init__(self, key=None, parent=None):
        self.key = key
        self.priority = random.randint(1, 1001)  # spezial case check smaller
        self.left_node = None
        self.right_node = None
        self.parent_node = parent
        self.xpos = 0
        self.color = "palegreen"

    def set_color_default(self, key, graph_list, treap):
        pass

    """
    Return-value :type NODE
    Graph_list   :type 
    """

    def insert(self, key, treap, parent=None):
        animation_handler = ah.AnimationHandler()
        tmp_graph = tr.TreapGraph(treap)
        tmp = self
        if key == self.key:
            #messagebox.showinfo("Warning", f"{key} already in Treap! Ignoring this entry")
            return tmp
        if self.key is None:
            self.color = "red"
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 2)
            self.key = key
            self.color = "palegreen"
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 3)
            return tmp

        elif key < self.key:
            if not self.left_node:
                self.left_node = Node(key, self)
                self.left_node.color = "palegreen"
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 2)
                if self.left_node.priority > self.priority:
                    tmp = self.left_node.rotate_right()
                    animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 2)
                return tmp
            else:
                self.left_node.color ="orange"
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 2)
                self.left_node.color = "palegreen"
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 2)
                self.left_node.insert(key, treap, self)
        else:
            if not self.right_node:
                self.right_node = Node(key, self)
                self.right_node.color = "palegreen"
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 2)
                if self.right_node.priority > self.priority:
                    tmp = self.right_node.rotate_left()
                    animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 2)
                return tmp
            else:
                self.right_node.color = "orange"
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 2)
                self.right_node.color = "palegreen"
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 2)
                self.right_node.insert(key, treap, self)

        while tmp.parent_node:
            tmp = tmp.parent_node
        return tmp

    def find(self, key, treap):
        if self.key is None:
            return False
        animation_handler = ah.AnimationHandler()
        tmp_graph = tr.TreapGraph(treap)
        if self.parent_node is None:
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 0)
        if self.key == key:
            tmp = self
            tmp.color = "red"
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 2)
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 3)
        elif key < self.key:
            if self.left_node:
                self.color = "grey"
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 4)
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 5)
                tmp = self.left_node.find(key, treap)
            else:
                return False
        else:
            if self.right_node:
                self.color = "grey"
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 6)
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 7)
                tmp = self.right_node.find(key, treap)
            else:
               # messagebox.showinfo("Error in find", f"Treap does not contain : {key}")
                return False
        return tmp

    """
    :return node 
    """

    # Todo: Cases checken , problems with deleting the root !!! rotations are working abs. fine
    def delete(self, key, graph_list, treap):
        # Case 0 : key not in Treap
        # this case gets handelt in function : find(self, key)
        tmp = self.find(key, graph_list, treap)
        # Case 1 : node to be deleted is a Leaf
        if tmp.left_node is None and tmp.right_node is None:
            # Node to be deleted is not Root
            if tmp.parent_node is not None:
                # Node is left-Node from Parents perspective
                if tmp.parent_node.left_node == tmp:
                    tmp.parent_node.left_node = None
                    return tmp
                # Node is right_node from Parents perspective
                else:
                    tmp.parent_node.right_node = None
                    return tmp
            # Node is Root
            # TODO mit clear vllt arbeiten !!
            else:
                tmp.key = None
                tmp.priority = random.randint(1, 1001)  # sonst wird nur key gelöscht prio w+rde gleich bleiebn ohne

                return tmp

        # Case 2.1: Node to be deleted has no left but a right node
        elif tmp.left_node is None and tmp.right_node is not None:
            # Node  is left_node from Parents perspective
            if tmp.parent_node and tmp.parent_node.left_node == tmp:
                tmp.parent_node.left_node = tmp.right_node
                tmp.right_node.parent_node = tmp.parent_node
                tmp = None
                return tmp
            # Node is right_node from Parents perspective
            elif tmp.parent_node and tmp.parent_node.right_node:
                tmp.parent_node.right_node = tmp.right_node
                tmp.right_node.parent_node = tmp.parent_node
                tmp = None
                return tmp
            # Node is root
            else:
                tmp.key = tmp.right_node.key
                tmp.right_node.parent_node = None
                if tmp.right_node.left_node is not None:
                    tmp.left_node = tmp.right_node.left_node
                    tmp.left_node.parent_node = tmp
                if tmp.right_node.right_node is not None:
                    tmp.right_node = tmp.right_node.right_node
                    tmp.right_node.parent_node = tmp
                tmp.right_node = None
                return tmp

        # Case 2.2 : Node to be deleted has no right but a left node
        elif tmp.left_node and not tmp.right_node:
            # Node is left-Node from Parents perspective
            if tmp.parent_node and tmp.parent_node.left_node == tmp:
                tmp.parent_node.left_node = tmp.left_node
                tmp.left_node.parent_node = tmp.parent_node
                tmp = None
                return tmp
            # Node is right_node from Parents perspective
            elif tmp.parent_node and tmp.parent_node.right_node == tmp:
                tmp.parent_node.right_node = tmp.left_node
                tmp.left_node.parent_node = tmp.parent_node
                tmp = None
                return tmp
            # Node is root
            else:
                tmp.key = tmp.left_node.key
                tmp.left_node.parent_node = None
                if tmp.left_node.right_node is not None:
                    tmp.right_node = tmp.left_node.right_node
                    tmp.right_node.parent_node = tmp
                if tmp.left_node.left_node is not None:
                    tmp.left_node = tmp.left_node.left_node
                    tmp.left_node.parent_node = tmp
                tmp.left_node = None
                return tmp
        # Case 3 : Node has a left and right Node
        else:
            tmp.priority = -math.inf
            tmp.move_down()
            tmp.delete(key, graph_list)
        return tmp

    # Moving a Node trough left/right rotation down
    def move_down(self):
        if self.left_node.priority > self.right_node.priority:
            self.left_node.rotate_right()
        else:
            self.right_node.rotate_left()
        return self

    def rotate_left(self):
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
        if self.parent_node is not None and self.priority > self.parent_node.priority:
            if self.parent_node.left_node == self:
                self.rotate_right()
            else:
                self.rotate_left()
        return self

    def rotate_right(self):
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
        if self.parent_node is not None and self.priority > self.parent_node.priority:
            if self.parent_node.left_node == self:
                self.rotate_right()
            else:
                self.rotate_left()
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
        if self.left_node:
            self.left_node.clear_colors()
        if self.right_node:
            self.right_node.clear_colors()
