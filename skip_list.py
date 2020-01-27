import math
import random as rd
import skip_list_graph as sl
import animation_handler as ah


# Skip Nodes have a set value and a list
# The list simply contains pointers of the next Skip Node of the same level

class SkipNode:
    def __init__(self, value, max_level):
        self.value = value
        self.height = self.set_height(max_level)
        self.list = [None] * self.height
        self.colors = ["palegreen"] * self.height

    # Returns random height smaller or equal to max_level
    # The height you get here is okay because of the array starting at 0
    def set_height(self, max_level):
        height = 1
        flag = True
        while flag:
            if rd.random() > 0.5:
                height += 1
            else:
                flag = False
        if height > max_level -1:
            return max_level -1
        else:
            return height

class BorderNode:
    def __init__(self, value, max_level):
        self.value = value
        self.height = max_level
        self.list = [None] * max_level
        self.colors = ["palegreen"] * max_level

# SkipList manages a set of SkipNodes
# This class offers the functions find, insert and delete
# Naming convention for the Nodes: x_ly, whereas x is the value and y is the level

class SkipList:

    def __init__(self):
        self.max_level = 1  # Initial value for the maximum height
        self.end = BorderNode(math.inf, self.max_level) # Right outer border
        self.root = BorderNode(-math.inf, self.max_level)  # Root
        self.root.list[0] = self.end  # Setting the first pointer
        self.number_of_elements = 0  # Num of elements not including -/+ inf
        self.position_list = [-math.inf, math.inf]
        self.had_elements = False
        


    def get_xpos(self, value):
        index = 0
        while index <= len(self.position_list):
            if self.position_list[index] == value:
                return index
            index += 1

    def insert_position_list(self, value):
        self.position_list.append(value)
        self.position_list.sort()

    def delete_position_list(self, value):
        self.position_list.remove(value)

    # Recalculates the max level of the skip list based on the log2 of the number of elements
    # max_so_far prevents the level from decreasing after deleting elements
    def recalculate_max_level(self):
        if self.number_of_elements == 1 and self.had_elements is False:
            self.root.height = 2
            self.end.height = 2
            self.increment_borders()
            self.had_elements = True
            return 2
        elif self.number_of_elements < 3:
            return 2
        else:
            max_so_far = self.max_level
            new_max_level = math.ceil(math.log2(self.number_of_elements))
            if new_max_level > max_so_far:
                self.root.height = new_max_level
                self.end.height = new_max_level
                self.increment_borders()
            return new_max_level if new_max_level > max_so_far else max_so_far


    # Function increment_borders increments the level of the borders by one
    def increment_borders(self):
        self.root.list.append(self.end)
        self.end.list.append(None)
        self.root.colors.append("palegreen")
        self.end.colors.append("palegreen")


    # search_level keeps track of the level that were in
    # Each element in a list points towards the next list that contains the next
    # value smaller than the value to be found but with a proper height
    # Function returns the found value always at level 0, else returns value 0 with an error message

    def find(self, value):
        self.clear_colors()
        compare_color = "orange"
        current_color = "salmon"
        path_color = "dimgrey"
        animation_handler = ah.AnimationHandler()
        search_level = self.max_level - 1  # Array starts at 0
        tmp = self.root  # Tmp keeps track of current list
        tmp_graph = sl.SkipListGraph()
        tmp.colors[search_level] = current_color  # Set the starting node ( top left corner ) to salmon
        animation_handler.push(tmp_graph.create_graph(self), "skip_list", "./res/skip_list_search.txt", 2)

        while True: #until value is either found or not
            while value >= tmp.list[search_level].value:  # The next skip node is smaller or equal to value
                tmp.list[search_level].colors[search_level] = compare_color # Set the next skip node color
                animation_handler.push(tmp_graph.create_graph(self), "skip_list", "./res/skip_list_search.txt", 4)
                tmp.list[search_level].colors[search_level] = current_color # Set the current node to salmon
                tmp.colors[search_level] = path_color # And the last one back to the standard color
                animation_handler.push(tmp_graph.create_graph(self), "skip_list", "./res/skip_list_search.txt", 5)
                tmp = tmp.list[search_level]  # Go right until overshoot
            if search_level == 0:  # At this point we should have found the value
                if value == tmp.value:
                    tmp.colors[search_level] = "peachpuff"
                    animation_handler.push(tmp_graph.create_graph(self), "skip_list", "./res/skip_list_search.txt", 0)
                    return animation_handler.get_instance().skip_list_graph_list
                else:
                    tmp.list[search_level].colors[search_level] = compare_color  # Set the next skip node color
                    animation_handler.push(tmp_graph.create_graph(self), "skip_list", "./res/skip_list_search.txt", 9)
                    tmp.list[search_level].colors[search_level] = current_color  # Set the current node to salmon
                    tmp.colors[search_level] = path_color  # And the last one back to the standard color
                    animation_handler.push(tmp_graph.create_graph(self), "skip_list", "./res/skip_list_search.txt", 10)
                    return 0
            else: # The case in which were going down a level
                tmp.list[search_level].colors[search_level] = compare_color # Set the next skip node color
                animation_handler.push(tmp_graph.create_graph(self), "skip_list", "./res/skip_list_search.txt", 11)
                tmp.list[search_level].colors[search_level] = "palegreen" # If a node was compared but is not used in the path
                tmp.colors[search_level] = path_color
                search_level -= 1
                tmp.colors[search_level] = current_color  # Set the current node to salmon
                animation_handler.push(tmp_graph.create_graph(self), "skip_list", "./res/skip_list_search.txt", 4)

    # Search is not animated, just for backend purposes
    def search(self, value):
        search_level = self.max_level - 1  # Array starts at 0
        tmp = self.root  # Tmp keeps track of current list
        while True:
            while value >= tmp.list[search_level].value:  # The next Skip Node
                tmp = tmp.list[search_level]  # Go right until overshoot
            if search_level == 0:  # At this point we should have found the value
                if value == tmp.value:
                    return True
                else:
                    return False
            search_level -= 1

    # Since we increase the number of elements, we need to change the circumstances first
    # Starts to look from the level of the calculated height, then simply finds the spot where
    # the new value would be found and adds it in between

    def insert(self, value):
        if self.search(value):
            return
        self.insert_position_list(value)
        self.clear_colors()
        compare_color = "orange"
        current_color = "salmon"
        path_color = "dimgrey"
        animation_handler = ah.AnimationHandler()
        tmp_graph = sl.SkipListGraph()
        self.number_of_elements += 1  # Increasing the Skip Node count
        self.max_level = self.recalculate_max_level()  # Recalculating the new max level
        skip_node = SkipNode(value, self.max_level)
        search_level = skip_node.height - 1   # We cannot insert it above its height
        tmp = self.root  # Using tmp to find the right spot to insert
        tmp.colors[search_level] = current_color  # Set the starting node ( top left corner ) to salmon
        animation_handler.push(tmp_graph.create_graph(self), "skip_list", "./res/skip_list_insert.txt", 4)
        while search_level >= 0:
            tmp.colors[search_level] = current_color  # Set the starting node ( top left corner ) to salmon
            animation_handler.push(tmp_graph.create_graph(self), "skip_list", "./res/skip_list_insert.txt", 5)
            while value > tmp.list[search_level].value:  # Go right until overshoot
                tmp.list[search_level].colors[search_level] = compare_color # Set the next skip node color
                animation_handler.push(tmp_graph.create_graph(self), "skip_list", "./res/skip_list_insert.txt", 6)
                tmp.colors[search_level] = path_color  # Set the starting node ( top left corner ) to salmon
                tmp = tmp.list[search_level]
                tmp.colors[search_level] = current_color  # Set the starting node ( top left corner ) to salmon
                animation_handler.push(tmp_graph.create_graph(self), "skip_list", "./res/skip_list_insert.txt", 7)
            animation_handler.push(tmp_graph.create_graph(self), "skip_list", "./res/skip_list_insert.txt", 8)
            skip_node.list[search_level] = tmp.list[search_level]
            tmp.colors[search_level] = path_color
            tmp.list[search_level] = skip_node  # TODO Doing the necessary pointer stuff
            skip_node.colors[search_level] = "peachpuff"  # Set the starting node ( top left corner ) to salmon
            animation_handler.push(tmp_graph.create_graph(self), "skip_list", "./res/skip_list_insert.txt", 9)
            #tmp.list[search_level] = skip_node  # Doing the necessary pointer stuff
            if search_level >0:
                tmp.colors[search_level-1] = current_color  # Set the starting node ( top left corner ) to salmon
            search_level -= 1
            if search_level < 0:
                animation_handler.push(tmp_graph.create_graph(self), "skip_list", "./res/skip_list_insert.txt", 0)
                return
            animation_handler.push(tmp_graph.create_graph(self), "skip_list", "./res/skip_list_insert.txt", 10)

        self.clear_colors()
        animation_handler.insert_first(tmp_graph.create_graph(self), "skip_list", "./res/skip_list_insert.txt", 0)
        return

    # Does stuff to the skip list, then finds the node and deletes them one by one
    def delete(self, value):

        # Checking if the value can be deleted
        if not self.search(value):
            return
        animation_handler = ah.AnimationHandler()
        self.clear_colors()
        compare_color = "orange"
        current_color = "salmon"
        path_color = "dimgrey"
        self.number_of_elements -= 1
        search_level = self.max_level - 1 # Array starts at 0
        tmp = self.root
        tmp_graph = sl.SkipListGraph()
        animation_handler.insert_first(tmp_graph.create_graph_delete(self), "skip_list", "./res/skip_list_delete.txt", 0)

        while search_level >= 0:
            tmp.colors[search_level] = current_color  # Set the starting node ( top left corner ) to salmon
            animation_handler.push(tmp_graph.create_graph_delete(self), "skip_list", "./res/skip_list_delete.txt", 11)
            while value > tmp.value:
                tmp.list[search_level].colors[search_level] = compare_color # Set the next skip node color
                animation_handler.push(tmp_graph.create_graph_delete(self), "skip_list", "./res/skip_list_delete.txt", 5)

                if value == tmp.list[search_level].value:
                    tmp.list[search_level].colors[search_level] = "peachpuff"   # Node to be deleted has been found
                    animation_handler.push(tmp_graph.create_graph_delete(self), "skip_list", "./res/skip_list_delete.txt", 6)
                    tmp.colors[search_level] = path_color
                    if search_level == 0:
                        animation_handler.push(tmp_graph.create_graph_delete(self), "skip_list", "./res/skip_list_delete.txt", 7)
                        animation_handler.push(tmp_graph.create_graph_delete(self), "skip_list", "./res/skip_list_delete.txt", 8)
                        tmp.list[search_level] = tmp.list[search_level].list[search_level]  # Overwritten the old pointer
                        animation_handler.push(tmp_graph.create_graph_delete(self), "skip_list", "./res/skip_list_delete.txt", 9)
                        self.clear_colors()
                        self.delete_position_list(value)
                        animation_handler.push(tmp_graph.create_graph_delete(self), "skip_list", "./res/skip_list_delete.txt", 0)
                        return 0
                    """tmp.list[search_level].height -= 1
                    tmp.list[search_level].list.pop() #Consider this"""
                    tmp.list[search_level] = tmp.list[search_level].list[search_level]  #Overwritten the old pointer
                    animation_handler.push(tmp_graph.create_graph_delete(self), "skip_list", "./res/skip_list_delete.txt", 7)
                    break
#                elif math.inf == tmp.list[search_level].value:
                elif tmp.list[search_level].value > value:

                    tmp.colors[search_level] = path_color
                    tmp.list[search_level].colors[search_level] = "palegreen"
                    break

                tmp.colors[search_level] = path_color  # And the last one back to the standard color
                tmp = tmp.list[search_level]
                tmp.colors[search_level] = current_color  # And the last one back to the standard color
                animation_handler.push(tmp_graph.create_graph_delete(self), "skip_list", "./res/skip_list_delete.txt", 10)

            search_level -= 1
        return 0


    def clear_colors(self): # Resets the color of every node
        tmp = self.root
        while tmp.list[0] is not None:
            for i in range(len(tmp.colors)):
                tmp.colors[i] = "palegreen"
            tmp = tmp.list[0]