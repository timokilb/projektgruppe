import networkx as nx

class SkipListGraph:
    def __init__(self, skip_list=None):
        self.graph = nx.DiGraph()
        self.skip_list = skip_list

    def create_graph(self, skip_list):
        graph = nx.DiGraph()
        tmp = skip_list.root
        search_level = skip_list.max_level-1
        while search_level >= 0:
            xpos = 0
            while tmp is not None:
                graph.add_node(str(tmp.value) + "/" + str(search_level), pos=(skip_list.get_xpos(tmp.value), search_level), label=tmp.value, color=tmp.colors[search_level])
                if tmp.list[search_level] is not None:
                    graph.add_edge(str(tmp.value) + "/" + str(search_level), str(tmp.list[search_level].value) + "/" + str(search_level))  # This draws the horizontal arrows between elements
                if search_level < tmp.height-1:
                    graph.add_edge(str(tmp.value) + "/" + str(search_level+1), str(tmp.value) + "/" + str(
                        search_level))  # This draws the horizontal arrows between elements"""
                xpos += 1  # Updating x position
                tmp = tmp.list[search_level]
            tmp = skip_list.root
            search_level -= 1
        return graph

    def create_graph_delete(self, skip_list):
        graph = nx.DiGraph()
        tmp = skip_list.root
        search_level = skip_list.max_level-1
        while search_level >= 0:
            xpos = 0
            while tmp is not None:
                graph.add_node(str(tmp.value) + "/" + str(search_level), pos=(skip_list.get_xpos(tmp.value), search_level), label=tmp.value, color=tmp.colors[search_level])
                if tmp.list[search_level] is not None:
                    graph.add_edge(str(tmp.value) + "/" + str(search_level), str(tmp.list[search_level].value) + "/" + str(search_level))  # This draws the horizontal arrows between elements
                if search_level >= 1:
                    graph.add_edge(str(tmp.value) + "/" + str(search_level), str(tmp.value) + "/" + str(
                        search_level-1))  # This draws the horizontal arrows between elements"""
                xpos += 1  # Updating x position
                tmp = tmp.list[search_level]
            tmp = skip_list.root
            search_level -= 1
        return graph
    #


    # First calls up update graph, then draws it
    def draw(self, skip_list, plot, canvas):
        plot.clear()
        self.skip_list = skip_list
        self.graph = self.create_graph(self.skip_list)
        pos = nx.get_node_attributes(self.graph, 'pos')
        label = nx.get_node_attributes(self.graph, 'label')
        color_dict = nx.get_node_attributes(self.graph, 'color')
        color_list = []
        for color in color_dict:
            color_list.append(color_dict[color])
        nx.draw(self.graph, pos, node_size=700, node_color=color_list, labels=label, with_labels=True, ax=plot)
        canvas.draw()
