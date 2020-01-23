import networkx as nx

class SkipListGraph:
    def __init__(self, skip_list=None):
        self.graph = nx.DiGraph()
        self.skip_list = skip_list

    # def set_skip_list(self, skip_list):

    # Here the graph is getting updated
    def create_graph(self, skip_list):
        graph = nx.DiGraph()
        tmp = skip_list.root
        xpos = 0
        while tmp is not None:
            ypos = 0
            for i in range(tmp.height):
                graph.add_node(str(tmp.value) + "/" + str(ypos), pos=(xpos, ypos), label=tmp.value, color=tmp.colors[i])
                if tmp.list[i] is not None:
                    graph.add_edge(str(tmp.value) + "/" + str(ypos), str(tmp.list[i].value) + "/" + str(
                        ypos))  # This draws the horizontal arrows between elements
                ypos += 1
            for element in range(len(tmp.list) - 1):
                graph.add_edge(str(tmp.value) + "/" + (str(element + 1)),
                               str(tmp.value) + "/" + str(element))  # This draws the vertical arrows between elements
            tmp = tmp.list[0] # TODO: Probably Here Lies the problem, because while inserting tmp.list[0] has no entry
            xpos += 1  # Updating x position
        return graph
    #TODO: Iterate horizontally first, then vertically maybe???

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
