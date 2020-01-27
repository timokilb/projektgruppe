import random
import math
import treap_graph as tr
import animation_handler as ah
import log_widget as log


class Node:

    def __init__(self, key=None, parent=None):
        self.key = key
        self.priority = random.randint(1, 1001)
        self.left_node = None
        self.right_node = None
        self.parent_node = parent
        self.xpos = 0
        self.color = "palegreen"

    def insert(self, key, treap, parent=None):
        global log_message
        animation_handler = ah.AnimationHandler()
        tmp_graph = tr.TreapGraph(treap)
        tmp = self

        if self.parent_node is None:
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 0)

        if key == self.key:
            self.color = "salmon"
            log_widget = log.LogWidget()
            log_widget.push(f"{key} ALREADY IN TREAP")
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 0)
            return

        if self.key is None:
            self.color = "salmon"
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 2)
            self.key = key
            self.color = "palegreen"
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 3)

        elif key <= self.key:
            self.color = "dimgrey"
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 4)
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 5)

            if not self.left_node:
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 2)
                self.left_node = Node(key, self)
                self.left_node.color = "salmon"
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 3)
                self.left_node.color = "palegreen"
                if self.left_node.priority > self.priority:
                    animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 6)
                    tmp = self.left_node.rotate_right(treap)
                self.default_color()
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 0)
            else:
                self.left_node.insert(key, treap, self)

        else:
            self.color = "dimgrey"
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 8)
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 9)

            if not self.right_node:
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 2)
                self.right_node = Node(key, self)
                self.right_node.color = "salmon"
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 3)
                self.right_node.color = "palegreen"
                if self.right_node.priority > self.priority:
                    animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 8)
                    tmp = self.right_node.rotate_left(treap)
                self.default_color()
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_insert.txt", 0)
            else:
                self.right_node.insert(key, treap, self)
        while tmp.parent_node:
            tmp = tmp.parent_node
        tmp.default_color()

    # find with animation
    def find(self, key, treap):
        animation_handler = ah.AnimationHandler()
        tmp_graph = tr.TreapGraph(treap)
        if self.key is None:
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 0)
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 8)
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 9)
            return self
        if self.parent_node is None:
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 0)
        if self.key == key:
            tmp = self
            tmp.color = "salmon"
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 2)
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 3)
            return tmp
        elif key <= self.key:
            if self.left_node:
                self.color = "dimgrey"
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 4)
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 5)
                tmp = self.left_node.find(key, treap)
            else:
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 8)
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 9)
                return self
        else:
            if self.right_node:
                self.color = "dimgrey"
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 6)
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 7)
                tmp = self.right_node.find(key, treap)
            else:
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 8)
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_search.txt", 9)
                return self

        return tmp

    # find with color changes
    def find_node(self, key):
        if self.key == key:
            self.color = "salmon"
            return self
        elif key > self.key:
            self.color = "gray"
            return self.right_node.find_node(key)
        elif key <= self.key:
            self.color = "gray"
            return self.left_node.find_node(key)
        else:
            return

    def find_ohne(self, key):
        if self.key == key:
            return self
        elif key > self.key and self.right_node is not None:
             return self.right_node.find_ohne(key)
        elif key < self.key and self.left_node is not None:
             return self.left_node.find_ohne(key)
        else:
            return False


    def find2(self, key):
        print(f"comparing {key} to {self.key}")
        if self.key == key:
            return True
        elif key > self.key and self.right_node is not None:
            self.right_node.find_ohne(key)
        elif key < self.key and self.left_node is not None:
            self.left_node.find_ohne(key)
        else:
            return False

    def delete(self, key, treap):
        animation_handler = ah.AnimationHandler()
        tmp_graph = tr.TreapGraph(treap)
        animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 0)
        animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 2)
        if self.find2(key) is False:
            return
        tmp = self.find_ohne(key)
        tmp.color = "salmon"

        # Case 1 : node to be deleted is a Leaf
        if tmp.left_node is None and tmp.right_node is None:
            # Node to be deleted is not Root
            if tmp.parent_node is not None:
                # Node is left-Node from Parents perspective
                tmp.color = "salmon"
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 4)
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 5)

                if tmp.parent_node.left_node == tmp:
                    tmp.parent_node.left_node = None
                    tmp.color = "palegreen"
                    tmp.default_color()
                    tmp.clear_colors()
                    animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 0)

                    return
                # Node is right_node from Parents perspective
                else:
                    tmp.parent_node.right_node = None
                    animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 5)
                    tmp.default_color()
                    tmp.clear_colors()
                    animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 0)
                    return
            # Node is Root
            else:
                tmp.key = None
                tmp.priority = random.randint(1, 1001)
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 5)
                tmp.default_color()
                tmp.clear_colors()
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 0)
                return
        else:
            tmp.priority = -math.inf
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 3)
            if tmp.left_node is None:
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 9)
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 10)
                tmp.right_node.rotate_left(treap)
                tmp.delete(key, treap)
                return
            elif tmp.right_node is None:
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 6)
                animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 7)
                tmp.left_node.rotate_right(treap)
                tmp.delete(key, treap)
                return
            else:
                tmp.move_down(treap)
                tmp.delete(key, treap)
                return
        return

    def move_down(self, treap):
        animation_handler = ah.AnimationHandler()
        tmp_graph = tr.TreapGraph(treap)
        if self.left_node.priority > self.right_node.priority:
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 6)
            self.left_node.color = "orange"
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 7)
            self.left_node.rotate_right(treap)
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 8)
        elif self.right_node.priority > self.left_node.priority:
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 9)
            self.right_node.color = "orange"
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 10)
            self.right_node.rotate_left(treap)
            animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_delete.txt", 11)

    def rotate_left(self, treap):
        animation_handler = ah.AnimationHandler()
        tmp_graph = tr.TreapGraph(treap)
        # self ist der zu rotierende Knoten
        self.color = "salmon"
        if self.parent_node:
            self.parent_node.color = "orange"
        if self.left_node:
            self.left_node.color = "peachpuff"
        animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_rotate_left.txt", 0)

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
        animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_rotate_left.txt", 0)
        self.left_node.color = "palegreen"
        animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_rotate_left.txt", 0)
        if self.parent_node is not None and self.priority > self.parent_node.priority:
            if self.parent_node.left_node == self:
                self.rotate_right(treap)
            else:
                self.rotate_left(treap)
        self.clear_colors()
        return self

    def rotate_right(self, treap):
        animation_handler = ah.AnimationHandler()
        tmp_graph = tr.TreapGraph(treap)
        self.color = "salmon"
        if self.parent_node:
            self.parent_node.color = "orange"
        if self.right_node:
            self.right_node.color = "peachpuff"
        animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_rotate_right.txt", 0)

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

        animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_rotate_right.txt", 0)
        self.right_node.color = "palegreen"
        animation_handler.push(tmp_graph.create_graph(), "treap", "./res/treap_rotate_right.txt", 0)
        if self.parent_node is not None and self.priority > self.parent_node.priority:
            if self.parent_node.left_node == self:
                self.rotate_right(treap)
            else:
                self.rotate_left(treap)
        # self.color = "palegreen"
        self.clear_colors()
        return self

    def clear_colors(self):
        if self:
            self.color = "palegreen"
        if self.left_node:
            self.left_node.clear_colors()
        if self.right_node:
            self.right_node.clear_colors()

    def default_color(self):
        tmp = self
        while tmp.parent_node:
            tmp.color = "palegreen"
            tmp = tmp.parent_node
        tmp.color = "palegreen"
