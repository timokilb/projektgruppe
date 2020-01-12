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

    __instance = None

    def __init__(self, master=None):
        if not AnimationHandler.__instance:
            AnimationHandler.__instance = AnimationHandler.__AnimationHandler(master)

    def get_instance(self):
        return AnimationHandler.__instance

    def push(self, graph, graph_list, pseudocode, line):
        if graph_list == "skip_list":
            AnimationHandler.__instance.pseudocode_widget.restore_default()
            AnimationHandler.__instance.skip_list_graph_list.append(graph)
            tmp = [pseudocode, line]
            AnimationHandler.__instance.pseudocode_list.append(tmp)
        elif graph_list == "treap":
            AnimationHandler.__instance.pseudocode_widget.restore_default()
            AnimationHandler.__instance.treap_graph_list.append(graph)
            tmp = [pseudocode, line]
            AnimationHandler.__instance.pseudocode_list.append(tmp)
        else:
            print("ERR: graph_list must be one of the following strings: treap, skip_list")

    def clear(self):
        AnimationHandler.__instance.treap_graph_list.clear()
        AnimationHandler.__instance.skip_list_graph_list.clear()
        AnimationHandler.__instance.pseudocode_list.clear()

    def display(self, index):
        AnimationHandler.__instance.pseudocode_widget.set_color("palegreen", index)


"""
Wir rufen immer auf: update_canvas(skip_list_graph_list(index))
Dies geschieht aber in der window datei - also in window datei global
den animation handler verwalten, animationen immer in diesen pushen mit der push funktion
dann aber in window etc muss wegen update canvas ca. wie folgt stehen:

    
"""
