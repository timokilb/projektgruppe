import math
import random as rd
import window as wd
import skip_list_graph as sl


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
        self.had_elements = False


    # Recalculates the max level of the skip list based on the log2 of the number of elements
    # max_so_far prevents the level from decreasing after deleting elements
    def recalculate_max_level(self):
        # print("Number of elements:", self.number_of_elements)
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
                print(new_max_level, "is max level new")
                self.increment_borders()
            return new_max_level if new_max_level > max_so_far else max_so_far


    # Function increment_borders increments the level of the borders by one

    def increment_borders(self):
        print("incremented borders by one")
        self.root.list.append(self.end)
        self.end.list.append(None)
        self.root.colors.append("palegreen")
        self.end.colors.append("palegreen")


    # search_level keeps track of the level that were in
    # Each element in a list points towards the next list that contains the next
    # value smaller than the value to be found but with a proper height
    # Function returns the found value always at level 0, else returns value 0 with an error message

    def find(self, value, graph_list):
        compare_color = "orange"
        current_color = "salmon"
        path_color = "dimgrey"
        search_level = self.max_level - 1  # Array starts at 0
        tmp = self.root  # Tmp keeps track of current list
        tmp_graph = sl.SkipListGraph()
        tmp.colors[search_level] = current_color  # Set the starting node ( top left corner ) to salmon
        graph_list.append(tmp_graph.create_graph(self))  # Append it to the list of graphs
        while True: #until value is either found or not
            while value >= tmp.list[search_level].value:  # The next skip node is smaller or equal to value
                tmp.list[search_level].colors[search_level] = compare_color # Set the next skip node color
                graph_list.append(tmp_graph.create_graph(self))
                tmp.list[search_level].colors[search_level] = current_color # Set the current node to salmon
                tmp.colors[search_level] = path_color # And the last one back to the standard color
                graph_list.append(tmp_graph.create_graph(self))
                tmp = tmp.list[search_level]  # Go right until overshoot
            if search_level == 0:  # At this point we should have found the value
                if value == tmp.value:
                    print(tmp.value, "is in the Skip List with height", tmp.height)
                    return graph_list
                else:
                    tmp.list[search_level].colors[search_level] = compare_color  # Set the next skip node color
                    graph_list.append(tmp_graph.create_graph(self))
                    tmp.list[search_level].colors[search_level] = current_color  # Set the current node to salmon
                    tmp.colors[search_level] = path_color  # And the last one back to the standard color
                    graph_list.append(tmp_graph.create_graph(self))
                    print("Err: ", value, "is not in the Skip List")
                    return 0
            else: # The case in which were going down a level
                tmp.list[search_level].colors[search_level] = compare_color # Set the next skip node color
                graph_list.append(tmp_graph.create_graph(self))  # Append it to the list of graphs
                tmp.list[search_level].colors[search_level] = "palegreen" # If a node was compared but is not used in the path
                tmp.colors[search_level] = path_color
                search_level -= 1
                tmp.colors[search_level] = current_color  # Set the current node to salmon
                graph_list.append(tmp_graph.create_graph(self))  # Append it to the list of graphs


    # Search is not animated, just for backend purposes
    def search(self, value):
        search_level = self.max_level - 1  # Array starts at 0
        tmp = self.root  # Tmp keeps track of current list
        while True:
            while value >= tmp.list[search_level].value:  # The next Skip Node
                tmp = tmp.list[search_level]  # Go right until overshoot
            if search_level == 0:  # At this point we should have found the value
                if value == tmp.value:
                    print(tmp.value, "is in the Skip List with height", tmp.height)
                    return
                else:
                    print("Err: ", value, "is not in the Skip List")
                    return 0
            search_level -= 1

    # Since we increase the number of elements, we need to change the circumstances first
    # Starts to look from the level of the calculated height, then simply finds the spot where
    # the new value would be found and adds it in between

    def insert(self, value, graph_list):
        if self.search(value):
            print(f"{value} already in there know I'm sayyn")
            return
        compare_color = "orange"
        current_color = "salmon"
        path_color = "dimgrey"
        tmp_graph = sl.SkipListGraph()
        graph_list.append(tmp_graph.create_graph(self))  # Append it to the list of graphs


        self.number_of_elements += 1  # Increasing the Skip Node count
        self.max_level = self.recalculate_max_level()  # Recalculating the new max level
        skip_node = SkipNode(value, self.max_level)
        #print(value, "is initialized with height of: ", len(skip_node.list), "and height of: ", skip_node.height,  "while border height is ", self.root.height)
        search_level = skip_node.height - 1   # We cannot insert it above its height TODO: - 1 changed
        tmp = self.root  # Using tmp to find the right spot to insert
        while search_level >= 0:
            while value >= tmp.list[search_level].value:  # Go right until overshoot
                tmp = tmp.list[search_level]
            skip_node.list[search_level] = tmp.list[search_level]
            tmp.list[search_level] = skip_node  # Doing the necessary pointer stuff
            search_level -= 1
        #Test
        tmp = self.root
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.list[0]
            #Testend
        return

    # TODO: Funktion noch komplett broken momentan
    # Does stuff to the skip list, then finds the node and deletes them one by one
    def delete(self, value, graph_list):
        compare_color = "orange"
        current_color = "salmon"
        path_color = "dimgrey"
        tmp_graph = sl.SkipListGraph()
        graph_list.append(tmp_graph.create_graph(self))  # Append it to the list of graphs

        self.number_of_elements -= 1
        search_level = self.max_level -1 # Array starts at 0
        tmp = self.root
        while search_level >= 0:
            print("I WAs hERE ONECE at search level ", search_level)
            print("value to be delted is", value, "while tmp value is", tmp.value)
            while value > tmp.value:
                if value == tmp.list[search_level].value:
                    print("DOING A CHECKER", tmp.list[search_level].list[search_level].value, "in level ", search_level)  # TODO; Much wrong here
                    tmp.list[search_level] = tmp.list[search_level].list[search_level]  #Overwritten the old pointer
                tmp = tmp.list[search_level]
            search_level -= 1
            tmp = self.root
        print(value, "Is no more in the Skip List")
        return 0
        # TODO: Stop one before so you can delete the right one?
