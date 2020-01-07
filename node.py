import random
import math
import time
from tkinter import messagebox
import treap_graph as tr


class Node:

    def __init__(self, key=None, parent=None):
        self.key = key
        self.priority = random.randint(1, 1001)  # spezial case check smaller
        self.left_node = None
        self.right_node = None
        self.parent_node = parent
        self.xpos = 0
        self.color =None #"palegreen"

    def set_color_default(self, key, graph_list,treap):
        tmp_graph = tr.TreapGraph(treap)
        if self.key == key:
            tmp = self
            tmp.color = "palegreen"
            graph_list.append(tmp_graph.create_graph())  # Append it to the list of graphs
        elif key < self.key:
            if self.left_node:
                self.color = "palegreen"
                graph_list.append(tmp_graph.create_graph())  # Append it to the list of graphs
                self.left_node.set_color_default(key, graph_list, treap)
        else:
            if self.right_node:
                self.color = "palegreen"
                graph_list.append(tmp_graph.create_graph())  # Append it to the list of graphs
                self.right_node.set_color_default(key, graph_list, treap)


    """
    Return-value :type NODE
    Graph_list   :type 
    
    """
    def insert(self, key, graph_list, treap, parent=None):
        tmp_graph = tr.TreapGraph(treap)
        #graph_list.append(tmp_graph.create_graph())
        tmp = self
        if key == self.key:
            messagebox.showinfo("Warning", f"{key} already in Treap! Ignoring this entry")
            return tmp

        if self.key is None:
            self.key = key
            self.color = "palegreen"
            graph_list.append(tmp_graph.create_graph())  # Append it to the list of graphs
            return tmp

        elif key < self.key:
            if not self.left_node:
                self.left_node = Node(key, self)
                self.left_node.color = "palegreen"
                graph_list.append(tmp_graph.create_graph())  # Append it to the list of graphs

                if self.left_node.priority > self.priority:
                    tmp = self.left_node.rotate_right()
                   # graph_list.append(tmp_graph.create_graph())  # Append it to the list of graphs
                    # added rotated graph to list
                return tmp
            else:
                self.left_node.insert(key, graph_list,treap, self)
        else:
            if not self.right_node:
                self.right_node = Node(key, self)
                self.right_node.color = "palegreen"
                graph_list.append(tmp_graph.create_graph())
                if self.right_node.priority > self.priority:
                    tmp = self.right_node.rotate_left()
                   # graph_list.append(tmp_graph.create_graph())  # Append it to the list of graphs
                return tmp
            else:
                self.right_node.insert(key, graph_list, treap, self)

        while tmp.parent_node:
            tmp = tmp.parent_node
        return tmp


    """
    Return-value :type NODE
    Graph_list   :type  List
    """
    def find(self, key, graph_list, treap):
        tmp_graph = tr.TreapGraph(treap)
        if self.key == key:
            tmp = self
            tmp.color = "red"
            graph_list.append(tmp_graph.create_graph())  # Append it to the list of graphs
            self.set_color_default(key, graph_list,treap)
            graph_list.append(tmp_graph.create_graph())  # Append it to the list of graphs

        elif key < self.key:
            if self.left_node:
                self.color = "grey"
                graph_list.append(tmp_graph.create_graph())  # Append it to the list of graphs
                tmp = self.left_node.find(key, graph_list,treap)
            else:
                # print("Error : Key not found ")
                messagebox.showinfo("Error in find", f"Treap does not contain : {key}")
                return False
        else:
            if self.right_node:
                self.color = "grey"
                graph_list.append(tmp_graph.create_graph())  # Append it to the list of graphs
                tmp = self.right_node.find(key, graph_list, treap)
            else:
                messagebox.showinfo("Error in find", f"Treap does not contain : {key}")
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
            # TODO : gönn dir diesen case ! PRIO !!!
            # TODO : clear löscht struktur
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


