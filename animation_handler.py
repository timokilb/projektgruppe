# Synchronises the canvas and pseudocode by forcing you to push the same amount of
# each type and give them a mutual index that is iterated while displaying

import pseudocode_widget as pw

class AnimationHandler:

    class __AnimationHandler:

        def __init__(self):
            self.treap_graph_list = []
            self.skip_list_graph_list = []
            self.pseudocode_widget = pw.PseudocodeWidget()
            self.pseudocode_list = []

    __instance = None

    def __init__(self):
        if not AnimationHandler.__instance:
            AnimationHandler.__instance = AnimationHandler.__AnimationHandler()

    def push(self, graph, graph_list, pseudocode, line):
        if graph_list == "skip_list":
            self.pseudocode_widget.restore_default
            self.skip_list_graph_list.append(graph)
            tmp = [pseudocode, line]
            self.pseudocode_list.append(tmp)
        elif graph_list == "treap":
            self.pseudocode_widget.restore_default
            self.treap_graph_list.append(graph)
            tmp = [pseudocode, line]
            self.pseudocode_list.append(tmp)
        else:
            print("ERR: graph_list must be one of the following strings: treap, skip_list")


    def clear(self):
        self.treap_graph_list.clear()
        self.skip_list_graph_list.clear()
        self.pseudocode_list.clear()

    def display(self, index):
        self.pseudocode_widget.set_color("yellow", index)

"""
Wir rufen immer auf: update_canvas(skip_list_graph_list(index))
Dies geschieht aber in der window datei - also in window datei global
den animation handler verwalten, animationen immer in diesen pushen mit der push funktion
dann aber in window etc muss wegen update canvas ca. wie folgt stehen:

global animation_handler:
if treap or skiplist: je nachdem welcher eingestellt ist
    update_canvas(animation_handler.treap_list[index])
    update pseudocode_widget(animation_handler.pseudo_list[index])
    
Also noch in pseudocode widget funktion erstellen, die ein tupel aus (data.txt, line) nimmt und updated, sowas wie
"""