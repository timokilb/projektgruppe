# Synchronises the canvas and pseudocode by forcing you to push the same amount of
# each type and give them a mutual index that is iterated while displaying

import pseudocode_widget as pw


class AnimationHandler:
    class __AnimationHandler:
        def __init__(self, master=None):
            self.treap_graph_list = []
            self.skip_list_graph_list = []
            self.pseudocode_widget = pw.PseudocodeWidget(master)
            self.pseudocode_list = []
            self.treap_pseudocode_list = []
            self.skip_list_history = [[], []]
            self.treap_history = [[], []]
            self.skip_list_time_stamps = []
            self.treap_time_stamps = []

    __instance = None

    def __init__(self, master=None):
        if not AnimationHandler.__instance:
            AnimationHandler.__instance = AnimationHandler.__AnimationHandler(master)

    def get_instance(self):
        return AnimationHandler.__instance

    def push(self, graph, algorithm, pseudocode, line):
        if algorithm == "skip_list":
            AnimationHandler.__instance.pseudocode_widget.restore_default()
            AnimationHandler.__instance.skip_list_graph_list.append(graph)
            tmp = [pseudocode, line]
            AnimationHandler.__instance.pseudocode_list.append(tmp)
        elif algorithm == "treap":
            AnimationHandler.__instance.pseudocode_widget.restore_default()
            AnimationHandler.__instance.treap_graph_list.append(graph)
            tmp = [pseudocode, line]
            AnimationHandler.__instance.treap_pseudocode_list.append(tmp)
        else:
            print("ERR: graph_list must be one of the following strings: treap, skip_list")

    def insert_first(self, graph, algorithm, pseudocode, line):
        if algorithm == "skip_list":
            AnimationHandler.__instance.pseudocode_widget.restore_default()
            AnimationHandler.__instance.skip_list_graph_list.insert(0, graph)
            tmp = [pseudocode, line]
            AnimationHandler.__instance.pseudocode_list.insert(0, tmp)
        elif algorithm == "treap":
            AnimationHandler.__instance.pseudocode_widget.restore_default()
            AnimationHandler.__instance.treap_graph_list.insert(0, graph)
            tmp = [pseudocode, line]
            AnimationHandler.__instance.treap_pseudocode_list.insert(0, tmp)
        else:
            print("ERR: graph_list must be one of the following strings: treap, skip_list")

    def clear(self):
        AnimationHandler.__instance.treap_graph_list.clear()
        AnimationHandler.__instance.skip_list_graph_list.clear()
        AnimationHandler.__instance.pseudocode_list.clear()
        AnimationHandler.__instance.treap_pseudocode_list.clear()

    # load_command loads a series of graph and pseudocode tuples into the graph list, which acts as a buffer
    def load_command(self, index):
        AnimationHandler.__instance.skip_list_graph_list.clear()
        AnimationHandler.__instance.pseudocode_list.clear()

        skip_list_start = AnimationHandler.__instance.skip_list_time_stamps[index][0]
        skip_list_end = AnimationHandler.__instance.skip_list_time_stamps[index][1]

        AnimationHandler.__instance.treap_graph_list.clear()
        AnimationHandler.__instance.treap_pseudocode_list.clear()

        treap_start = AnimationHandler.__instance.treap_time_stamps[index][0]
        treap_end = AnimationHandler.__instance.treap_time_stamps[index][1]

        for i in range(skip_list_end - skip_list_start):
            AnimationHandler.__instance.skip_list_graph_list.append(
                AnimationHandler.__instance.skip_list_history[0][skip_list_start + i])
            AnimationHandler.__instance.pseudocode_list.append(
                AnimationHandler.__instance.skip_list_history[1][skip_list_start + i])

        for i in range(treap_end - treap_start):
            AnimationHandler.__instance.treap_graph_list.append(
                AnimationHandler.__instance.treap_history[0][treap_start + i])
            AnimationHandler.__instance.treap_pseudocode_list.append(
                AnimationHandler.__instance.treap_history[1][treap_start + i])