# Creating a Log Widget using singleton pattern
# Returns a series of strings where as the last inserted string appears on top

# How to use:
# use import LogWidget as lw
#   log_widget = LogWidget()
#   from where you want to write messages to the widget, use
#       log_widget.push("String")
#   to get the whole text, use log_widget.update()

import tkinter as tk


class PseudocodeWidget:
    class __PseudocodeWidget:

        def __init__(self, master):
            self.labels = [tk.Label(master=master),
                           tk.Label(master=master),
                           tk.Label(master=master),
                           tk.Label(master=master),
                           tk.Label(master=master),
                           tk.Label(master=master),
                           tk.Label(master=master),
                           tk.Label(master=master),
                           tk.Label(master=master),
                           tk.Label(master=master)]

            self.pseudocode_list = []

    __instance = None

    def __init__(self, master):
        if not PseudocodeWidget.__instance:  # There is no instance
            PseudocodeWidget.__instance = PseudocodeWidget.__PseudocodeWidget(master)

    def get_instance(self):
        return self.__instance

    def restore_default(self):
        # restore default values for all labels
        for entry in self.__instance.labels:
            entry.config(text="", bg="white")

    # returns label element at given index
    def get_label(self, position):
        return self.get_instance().labels[position]

    # returns Array/List with all labels
    def get_all_labels(self):
        all_label = []
        for element in self.get_instance().labels:
            all_label.append(element)
        return all_label

    def update_display(self):
        pass

    def update(self):
        print(self)
        print(PseudocodeWidget.__instance)

    def pack_labels(self):
        for element in self.get_instance().labels:
            element.pack(side="top", fill="both")

    def set_color(self, color, index):
        self.get_label(index)["bg"] = color
        self.update()

    # open File wich contains pseudocode
    def open_text_file(self, string):
        self.restore_default()
        file = open(string, mode="r")
        position = 0
        for line in file:
            PseudocodeWidget.__instance.labels[position].config(text=line, bg="#2b2b2b", fg="#a9b7c6", anchor="nw", font="helvetica, 16", height=1)
            position += 1
        # TODO wenn PseudoCode weniger als 10 zeilen hat , manuell auffüllen. ANDERN !!!
        while position < 10:
            PseudocodeWidget.__instance.labels[position].config(text="", bg="#2b2b2b", fg="#a9b7c6",
                                                                anchor="w")
            position += 1
        # PseudocodeWidget.__instance.pseudocode_list.append(PseudocodeWidget.__instance.labels)


if __name__ == "__main__":
    root = tk.Tk()
    widget = PseudocodeWidget(root)
    widget.update()
