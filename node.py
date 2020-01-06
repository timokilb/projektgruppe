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
        self.color ="palegreen"

    """
    Return-value :type NODE
    Graph_list   :type 
    
    """
    def insert(self, key, graph_list, parent=None):
        tmp = self
        if self.key is None:
            self.key = key
            graph_list.append(self)
            return self  # tmp vorher
        if key == self.key:
            messagebox.showinfo("Warning", f"{key} already in Treap! Ignoring this entry")
            return tmp
        elif key < self.key:
            if not self.left_node:
                self.left_node = Node(key, self)
                self.left_node.color = "green"
                # self.left_node.level = self.level + 1
                graph_list.append(self.left_node)
                if self.left_node.priority > self.priority:
                    self.left_node.color = "orange"
                    self.color = "purple"
                    graph_list.append(tmp) # tmp mayber
                    tmp = self.left_node.rotate_right()
                    # added rotated graph to list
                    graph_list.append(tmp) # tmp mayber
                return tmp
            else:
                self.left_node.color ="yellow"
                graph_list.append(self)
                self.left_node.insert(key, graph_list, self)
        else:
            if not self.right_node:
                self.right_node = Node(key, self)
                self.right_node.color = "blue"

                # self.right_node.level = self.level + 1
                graph_list.append(self.right_node)
                if self.right_node.priority > self.priority:
                    self.right_node.color = "orange"
                    self.color = "purple"
                    tmp = self.right_node.rotate_left()
                    graph_list.append(tmp) # tmp maybe 2 ?
                return tmp
            else:
                self.right_node.color ="yellow"
                graph_list.append(self)
                self.right_node.insert(key, graph_list, self)

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
    def delete(self, key, graph_list):
        # Case 0 : key not in Treap
        # this case gets handelt in function : find(self, key)
        tmp = self.find(key, graph_list)
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
